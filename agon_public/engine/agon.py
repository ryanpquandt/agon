#!/usr/bin/env python3
"""
Agon engine — deterministic gates over the markdown ledger.

Agon stays markdown-native: the project record (`projects/<name>/record.md`) is
the single, human-editable source of truth. This engine parses its `## Ledger`
section (a strict one-line-per-event grammar) plus `brief.md`, and
enforces what must hold regardless of which model is driving:

  * phase-close gates (conceive / refine / plan / review / polish / done):
    the editor must actually have fired; every objection carries a ruling, a
    concession, or preserved dissent before closure; considered-and-rejected
    alternatives count only when rated strong|moderate with a reason;
  * brief-before-commit: thesis, outline, and altitude decisions are refused
    without a prior decision brief carrying >= 2 live options;
  * the draft cycle: a review cannot close without a full draft on the record,
    an editor objection engaging THAT draft, and an altitude decision
    (redirect | restructure | rework | descend | ship) briefed and committed
    after it; the polish funnel is reachable only through `descend`;
  * drafting rights (from brief.md's `- **Rights:**` line):
      fiction              — Agon writes no manuscript words, ever; the consent
                             mechanism itself is disabled (any consent/ai-draft
                             entry is a standing violation);
      nonfiction           — the human drafts; formulations only as options on
                             request (skill-layer); no ai-draft;
      technical-delegable  — an `ai-draft` is allowed ONLY with a prior human
                             `consent — reason: …` entry; the reason is logged
                             and permanent.

Ledger line grammar (one entry per line, inside `## Ledger`):

  - [YYYY-MM-DD] <type>: <text> — key: value — key: value

Types: decision, brief, objection, ruling, conceded, dissent-preserved,
declined, draft, consent, ai-draft, evidence, backward-flag, stage, note.

Stdlib only. Invoke from the agon root:
  python3 engine/agon.py <status|gate|log|selftest> ...
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

LEDGER_TYPES = {
    "decision", "brief", "objection", "ruling", "conceded",
    "dissent-preserved", "declined", "draft", "consent", "ai-draft",
    "evidence", "backward-flag", "stage", "note",
}
RATED_OK = {"strong", "moderate"}
ANSWERS = {"ruling", "conceded", "dissent-preserved"}
ALTITUDES = {"redirect", "restructure", "rework", "descend", "ship"}
RIGHTS = {"fiction", "nonfiction", "technical-delegable"}
GATES = ["conceive", "refine", "plan", "review", "polish", "done"]

LINE_RE = re.compile(r"^- \[(\d{4}-\d{2}-\d{2})\] ([a-z-]+): (.*)$")


class Entry:
    def __init__(self, date: str, type_: str, rest: str, lineno: int):
        self.date, self.type, self.lineno = date, type_, lineno
        parts = [p.strip() for p in rest.split(" — ")]
        self.text = parts[0]
        self.fields: dict[str, str] = {}
        for p in parts[1:]:
            if ": " in p:
                k, v = p.split(": ", 1)
                self.fields[k.strip().lower()] = v.strip()


def resolve_project(name: str) -> Path:
    p = Path(name)
    if p.is_dir():
        return p
    for base in (Path("projects"),
                 Path(__file__).resolve().parent.parent / "projects"):
        if (base / name).is_dir():
            return base / name
    sys.exit(f"error: project not found: {name}")


def parse_ledger(proj: Path) -> list[Entry]:
    rec = proj / "record.md"
    if not rec.exists():
        return []
    entries, in_ledger, in_comment = [], False, False
    for i, line in enumerate(rec.read_text(encoding="utf-8").splitlines(), 1):
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if "<!--" in line:
            if "-->" not in line:
                in_comment = True
            continue
        if line.startswith("## "):
            in_ledger = line.strip().lower().startswith("## ledger")
            continue
        if not in_ledger:
            continue
        m = LINE_RE.match(line.strip())
        if m:
            e = Entry(m.group(1), m.group(2), m.group(3), i)
            if e.type in LEDGER_TYPES:
                entries.append(e)
    return entries


def brief_field(proj: Path, name: str) -> str | None:
    b = proj / "brief.md"
    if not b.exists():
        return None
    m = re.search(
        rf"^- \*\*{name}:\*\*\s*`?([A-Za-z0-9_ /:.+-]+?)`?\s*(?:<!--.*)?$",
        b.read_text(encoding="utf-8"), re.MULTILINE,
    )
    return m.group(1).strip() if m else None


def rights_of(proj: Path) -> str:
    r = (brief_field(proj, "Rights") or "nonfiction").lower()
    return r if r in RIGHTS else "nonfiction"


def window_since_stage(entries: list[Entry]) -> list[Entry]:
    last = None
    for i, e in enumerate(entries):
        if e.type == "stage":
            last = i
    return entries if last is None else entries[last + 1:]


def latest_draft(entries: list[Entry]) -> Entry | None:
    ds = [e for e in entries if e.type == "draft"]
    return ds[-1] if ds else None


# ---- shared checks ----------------------------------------------------------

def _check_objections(win: list[Entry], missing: list[str], require=True,
                      label="this phase"):
    obj = [e for e in win if e.type == "objection"]
    ans = [e for e in win if e.type in ANSWERS]
    if require and not obj:
        missing.append(f"no objection logged {label} — the editor has not "
                       f"fired; dispatch the agonistic-editor")
    if len(ans) < len(obj):
        missing.append(f"{len(obj) - len(ans)} objection(s) unanswered — log "
                       f"the writer's ruling / a concession / preserved "
                       f"dissent for each")


def _check_declined(win: list[Entry], missing: list[str], what: str):
    ok = [e for e in win if e.type == "declined"
          and e.fields.get("rated") in RATED_OK]
    unrated = [e for e in win if e.type == "declined" and e not in ok]
    if not ok:
        msg = (f"no {what} logged considered-and-declined, rated "
               f"strong|moderate by the editor")
        if unrated:
            msg += (f" ({len(unrated)} on record lack a qualifying rating — "
                    f"presumed straw until rated)")
        missing.append(msg)


def _check_brief_before(entries: list[Entry], decides: str,
                        missing: list[str], after_line: int = 0):
    def _n(e):
        try:
            return int(e.fields.get("options", "0"))
        except ValueError:
            return 0
    scope = [e for e in entries if e.lineno > after_line]
    briefs = [e for e in scope if e.type == "brief"
              and e.fields.get("decides") == decides and _n(e) >= 2]
    decisions = [e for e in scope if e.type == "decision"
                 and e.fields.get("decides") == decides]
    if not decisions:
        missing.append(f"no decision logged with decides: {decides}")
        return None
    if not briefs or briefs[0].lineno > decisions[-1].lineno:
        missing.append(
            f"decision '{decides}' committed without a prior brief carrying "
            f">= 2 live options (brief — decides: {decides} — options: N) — "
            f"a single option is a fait accompli")
    return decisions[-1]


def _check_rights(proj: Path, entries: list[Entry], missing: list[str]):
    rights = rights_of(proj)
    consents = [e for e in entries if e.type == "consent"]
    drafts_ai = [e for e in entries if e.type == "ai-draft"]
    if rights == "fiction":
        for e in consents + drafts_ai:
            missing.append(
                f"{e.type} at line {e.lineno} in a FICTION project — Agon "
                f"writes no manuscript words in fiction and the consent "
                f"mechanism is disabled; this is a standing violation")
        return
    for e in drafts_ai:
        if rights != "technical-delegable":
            missing.append(
                f"ai-draft at line {e.lineno} but Rights is '{rights}' — "
                f"delegated drafting requires Rights: technical-delegable "
                f"in brief.md")
            continue
        prior = [c for c in consents if c.lineno < e.lineno
                 and c.fields.get("reason")]
        if not prior:
            missing.append(
                f"ai-draft at line {e.lineno} without a prior consent "
                f"carrying a reason (consent: <go-ahead> — reason: <why "
                f"delegation is right here>) — the go-ahead and the why are "
                f"both required, and they are permanent")


# ---- the gates --------------------------------------------------------------

def gate(proj: Path, stage: str) -> tuple[bool, list[str]]:
    entries = parse_ledger(proj)
    win = window_since_stage(entries)
    missing: list[str] = []

    if not entries:
        return False, ["record.md has no parseable '## Ledger' entries — "
                       "nothing on the record means nothing happened"]

    _check_rights(proj, entries, missing)

    if stage in ("conceive", "refine"):
        _check_objections(win, missing)
        _check_brief_before(entries, "thesis", missing)
        _check_declined(win, missing,
                        "alternative thesis/question/framing")
    elif stage == "plan":
        _check_objections(win, missing)
        _check_brief_before(entries, "outline", missing)
        _check_declined(win, missing, "structural alternative")
    elif stage == "review":
        d = latest_draft(entries)
        if d is None:
            missing.append("no draft on the record (draft: <desc> — id: "
                           "draft-NN) — the writing room has not returned; "
                           "there is nothing to review")
        else:
            after = [e for e in entries if e.lineno > d.lineno]
            _check_objections(after, missing,
                              label=f"since {d.fields.get('id', 'the draft')}")
            dec = _check_brief_before(entries, "altitude", missing,
                                      after_line=d.lineno)
            if dec is not None:
                choice = (dec.fields.get("choice") or "").lower()
                if choice not in ALTITUDES:
                    missing.append(
                        f"altitude decision at line {dec.lineno} needs "
                        f"choice: {'|'.join(sorted(ALTITUDES))}")
    elif stage == "polish":
        d = latest_draft(entries)
        alts = [e for e in entries if e.type == "decision"
                and e.fields.get("decides") == "altitude"
                and (d is None or e.lineno > d.lineno)]
        choice = (alts[-1].fields.get("choice") or "").lower() if alts else None
        if choice not in ("descend", "ship"):
            missing.append(
                f"the polish funnel is reachable only through an altitude "
                f"decision of 'descend' (latest: {choice or 'none'}) — do not "
                f"polish sentences in a draft that may be redirected, "
                f"restructured, or reworked wholecloth")
    elif stage == "done":
        _check_objections(entries, missing, require=False, label="anywhere")
        if latest_draft(entries) is None:
            missing.append("no draft ever logged — a project cannot finish "
                           "without a draft cycle on the record")
        alts = [e for e in entries if e.type == "decision"
                and e.fields.get("decides") == "altitude"]
        if not alts or (alts[-1].fields.get("choice") or "").lower() not in (
                "descend", "ship"):
            missing.append("the last altitude decision must be descend|ship "
                           "before the project closes")
    else:
        return False, [f"unknown stage {stage!r} (use {'/'.join(GATES)})"]

    return (not missing), missing


# ---- commands ---------------------------------------------------------------

def cmd_status(args):
    proj = resolve_project(args.project)
    entries = parse_ledger(proj)
    counts: dict[str, int] = {}
    for e in entries:
        counts[e.type] = counts.get(e.type, 0) + 1
    win = window_since_stage(entries)
    obj = sum(1 for e in win if e.type == "objection")
    ans = sum(1 for e in win if e.type in ANSWERS)
    print(f"project: {proj.name}")
    print(f"status: {brief_field(proj, 'Status') or '?'}")
    print(f"rights: {rights_of(proj)}")
    print(f"ledger entries: {len(entries)}  "
          + " ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(f"current window: {len(win)} entr(y/ies), "
          f"open objections: {max(0, obj - ans)}")
    ds = [e for e in entries if e.type == "draft"]
    if ds:
        print("draft cycle:")
        for d in ds:
            after = [e for e in entries if e.lineno > d.lineno]
            alt = next((e.fields.get("choice") for e in after
                        if e.type == "decision"
                        and e.fields.get("decides") == "altitude"), None)
            print(f"  - {d.fields.get('id', '?')}: "
                  f"altitude={alt or 'UNREVIEWED'}")
    viol: list[str] = []
    _check_rights(proj, entries, viol)
    for v in viol:
        print(f"RIGHTS VIOLATION: {v}")


def cmd_gate(args):
    proj = resolve_project(args.project)
    ok, missing = gate(proj, args.stage)
    print(f"stage: {args.stage}")
    print(f"can_close: {ok}" if args.stage not in ("polish",)
          else f"can_enter: {ok}")
    for m in missing:
        print(f"  - {m}")
    sys.exit(0 if ok else 1)


def cmd_log(args):
    proj = resolve_project(args.project)
    if args.type not in LEDGER_TYPES:
        sys.exit(f"error: type must be one of {sorted(LEDGER_TYPES)}")
    date = args.date or _dt.date.today().isoformat()
    line = f"- [{date}] {args.type}: {args.text}"
    for kv in (args.field or []):
        if "=" not in kv:
            sys.exit(f"error: --field needs key=value, got {kv!r}")
        k, v = kv.split("=", 1)
        line += f" — {k.strip()}: {v.strip()}"
    rec = proj / "record.md"
    text = rec.read_text(encoding="utf-8") if rec.exists() else "# Record\n"
    if re.search(r"^## Ledger", text, re.MULTILINE) is None:
        text = text.rstrip() + "\n\n## Ledger\n"
    m = re.search(r"^## Ledger.*?$(.*?)(?=^## |\Z)", text,
                  re.MULTILINE | re.DOTALL)
    insert_at = m.end(1)
    text = text[:insert_at].rstrip() + "\n" + line + "\n" + text[insert_at:]
    rec.write_text(text, encoding="utf-8")
    print(f"logged: {line}")


# ---- selftest ---------------------------------------------------------------

def cmd_selftest(_args):
    import tempfile
    fails: list[str] = []

    def expect(cond: bool, label: str):
        print(("  ok  " if cond else "  FAIL") + f" {label}")
        if not cond:
            fails.append(label)

    def make_proj(td, name, rights):
        proj = Path(td) / name
        proj.mkdir()
        (proj / "brief.md").write_text(
            f"# Brief\n\n- **Status:** `conceive`\n- **Rights:** `{rights}`\n")
        (proj / "record.md").write_text("# Record\n\n## Ledger\n")
        return proj

    def log(proj, t, text, **kw):
        line = f"- [2026-07-02] {t}: {text}"
        for k, v in kw.items():
            line += f" — {k.replace('_', '-')}: {v}"
        rec = proj / "record.md"
        rec.write_text(rec.read_text() + line + "\n")

    with tempfile.TemporaryDirectory() as td:
        # -- nonfiction essay: the draft-cycle spine --------------------------
        p = make_proj(td, "essay", "nonfiction")
        ok, why = gate(p, "conceive")
        expect(not ok, "empty ledger blocks conceive close")
        log(p, "decision", "thesis committed", decides="thesis")
        ok, why = gate(p, "conceive")
        expect(not ok and any("fait accompli" in m for m in why),
               "thesis without prior brief blocks")
        log(p, "brief", "two theses tabled", decides="thesis", options="2")
        log(p, "decision", "thesis re-committed", decides="thesis")
        log(p, "objection", "thesis assumes the mechanism", by="editor",
            demand="cite or hedge")
        log(p, "ruling", "mechanism claim narrowed")
        log(p, "declined", "the broader survey framing", rated="moderate")
        ok, why = gate(p, "conceive")
        expect(ok, "conceive closes with brief + contest + rated decline")

        log(p, "stage", "conceive -> plan")
        log(p, "brief", "two arcs tabled", decides="outline", options="2")
        log(p, "decision", "problem-first arc", decides="outline")
        log(p, "objection", "section 3 does no work", by="editor",
            demand="cut or justify")
        log(p, "conceded", "section 3 cut")
        log(p, "declined", "chronological arc", rated="strong")
        ok, why = gate(p, "plan")
        expect(ok, "plan closes; the writing room opens")

        log(p, "stage", "plan -> draft")
        ok, why = gate(p, "review")
        expect(not ok and any("writing room" in m for m in why),
               "review blocks with no draft on the record")
        log(p, "draft", "full draft returned", id="draft-01")
        ok, why = gate(p, "review")
        expect(not ok and any("editor has not fired" in m for m in why),
               "review needs the editor to engage THIS draft")
        log(p, "objection", "middle sags; thesis lands late", by="editor",
            demand="restructure or cut")
        log(p, "ruling", "agreed: thesis holds, structure does not")
        log(p, "decision", "restructure", decides="altitude",
            choice="restructure")
        ok, why = gate(p, "review")
        expect(not ok and any("fait accompli" in m for m in why),
               "altitude decision needs its own brief")
        log(p, "brief", "altitudes tabled: restructure vs rework",
            decides="altitude", options="2")
        log(p, "decision", "restructure draft-01", decides="altitude",
            choice="restructure")
        ok, why = gate(p, "review")
        expect(ok, "review closes with briefed altitude decision")
        ok, why = gate(p, "polish")
        expect(not ok, "polish unreachable while altitude is restructure")

        log(p, "draft", "second full draft", id="draft-02")
        log(p, "objection", "para 4 evidence thin", by="editor",
            demand="cite or cut")
        log(p, "ruling", "citation added at line level later; noted")
        log(p, "brief", "altitudes tabled: rework vs descend",
            decides="altitude", options="2")
        log(p, "decision", "descend to polish", decides="altitude",
            choice="descend")
        ok, why = gate(p, "review")
        expect(ok, "second cycle closes")
        ok, why = gate(p, "polish")
        expect(ok, "polish reachable after descend")
        ok, why = gate(p, "done")
        expect(ok, "done gate passes with clean record")

        # -- fiction: the consent mechanism is disabled ------------------------
        f = make_proj(td, "novel", "fiction")
        log(f, "brief", "two premises tabled", decides="thesis", options="2")
        log(f, "decision", "premise committed", decides="thesis")
        log(f, "objection", "protagonist wants nothing", by="editor",
            demand="name the want")
        log(f, "ruling", "want named in ch.1")
        log(f, "declined", "the frame-story premise", rated="strong")
        ok, why = gate(f, "conceive")
        expect(ok, "fiction conceive closes normally")
        log(f, "consent", "please draft ch.2", reason="stuck")
        ok, why = gate(f, "conceive")
        expect(not ok and any("FICTION" in m for m in why),
               "consent entry in fiction is a standing violation")

        # -- technical-delegable: consent chain --------------------------------
        t = make_proj(td, "explainer", "technical-delegable")
        log(t, "brief", "two framings", decides="thesis", options="2")
        log(t, "decision", "framing set", decides="thesis")
        log(t, "objection", "audience too broad", by="editor", demand="narrow")
        log(t, "ruling", "narrowed to policymakers")
        log(t, "declined", "the FAQ format", rated="moderate")
        log(t, "ai-draft", "condensed version drafted", id="draft-01")
        ok, why = gate(t, "conceive")
        expect(not ok and any("without a prior consent" in m for m in why),
               "ai-draft without consent+reason blocks")
        log(t, "consent", "go ahead and draft the condensed version",
            reason="substantive original already human-drafted; this is a "
                   "non-expert condensation")
        log(t, "ai-draft", "condensed version drafted (consented)",
            id="draft-02")
        ok, why = gate(t, "conceive")
        expect(not ok, "earlier unconsented ai-draft still stands as violation")
        # a fresh project doing it right
        t2 = make_proj(td, "explainer2", "technical-delegable")
        log(t2, "brief", "two framings", decides="thesis", options="2")
        log(t2, "decision", "framing set", decides="thesis")
        log(t2, "objection", "audience too broad", by="editor", demand="narrow")
        log(t2, "ruling", "narrowed")
        log(t2, "declined", "the FAQ format", rated="strong")
        log(t2, "consent", "draft the condensed version",
            reason="original human-drafted at length; condensation delegated")
        log(t2, "ai-draft", "condensed version drafted", id="draft-01")
        ok, why = gate(t2, "conceive")
        expect(ok, "consented ai-draft passes in technical-delegable")

    print()
    if fails:
        print(f"SELFTEST: {len(fails)} failure(s)")
        sys.exit(1)
    print("SELFTEST: all checks passed")


# ---- entry ------------------------------------------------------------------

def main(argv=None):
    p = argparse.ArgumentParser(prog="agon",
                                description=__doc__.split("\n")[1])
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("status", help="orient: status/rights, ledger, cycles")
    s.add_argument("--project", required=True)
    s.set_defaults(func=cmd_status)

    s = sub.add_parser("gate", help="can this phase close (polish: be entered)?")
    s.add_argument("--project", required=True)
    s.add_argument("--stage", required=True, choices=GATES)
    s.set_defaults(func=cmd_gate)

    s = sub.add_parser("log", help="append a well-formed ledger line")
    s.add_argument("--project", required=True)
    s.add_argument("--type", required=True)
    s.add_argument("--text", required=True)
    s.add_argument("--field", action="append",
                   help="repeatable key=value (e.g. decides=altitude)")
    s.add_argument("--date", default=None)
    s.set_defaults(func=cmd_log)

    s = sub.add_parser("selftest", help="end-to-end check in a temp project")
    s.set_defaults(func=cmd_selftest)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
