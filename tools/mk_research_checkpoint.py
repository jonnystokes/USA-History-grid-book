import os, re, subprocess, sys
ROOT = r"C:\Users\jon\Projects\History-Book-Project-claude"
os.chdir(ROOT)
REG = open("control/chapter-registry.md", encoding="utf-8").read()
def registry(slug):
    for line in REG.splitlines():
        if f"| `{slug}` |" in line:
            c = [x.strip() for x in line.split("|")]
            return f"Registry: {c[3]}: {c[5]} Not: {c[6]}"
    return "Registry: see control/chapter-registry.md"
def measured(slug):
    out = subprocess.run(["python", "tools/project_state.py", "--check", slug, "--stage", "research"], capture_output=True, text=True).stdout
    m = re.search(r"measured: (.*)", out)
    return (out.splitlines()[0] if out else "?") + "\n  " + (m.group(1) if m else "?")
HARD = {
 "news-communication": "Who controlled the news and who was shut out (the Black press and attacks on it: Lovejoy 1837 and McIntosh parked in this bank; Ida B. Wells's press destroyed 1892) · the Sedition Act of 1798 and who was jailed · Native-language newspapers (the Cherokee Phoenix, 1828) · the telegraph's owners · propaganda and censorship in wartime · 2000-today: platforms, misinformation, and press freedom figures, dated.",
 "holidays": "Whose days became national holidays and whose did not, and who decided · Thanksgiving's origin story against the record (the Wampanoag, the 1621 harvest, the 1637 Pequot killings as later tied to the day by some writers: record every claim with its source) · Juneteenth (1865 and 2021) · Columbus Day and Indigenous Peoples' Day · holidays under slavery (Christmas 'holidays' on plantations, Pinkster, Negro Election Day) · Labor Day (parked here from work-workers).",
}
HARD["art"] = ("Physical art only (DECISIONS #7: music is its own chapter; #12: film lives in storytelling-evolution). "
 "Native art as the art of named nations, not generic 'Native art', and objects taken from Native graves and nations (NAGPRA 1990, the 2024 rules, museums' holdings, dated counts) · "
 "enslaved artisans (Dave the Potter, David Drake, with his inscriptions) · who was shut out of academies and museums · public art destroyed or removed, with who decided · the outline carries 115 [VERIFY] tags and 26 candidates: clear or honestly resolve each one in your eras.")
HARD["music"] = ("Music as its own chapter (DECISIONS #7). Native nations' music by named nation · music under slavery (spirituals, the banjo's African origin, laws banning drums after the 1739 Stono revolt) · who was paid and who was not (records, royalties, cover versions) · segregated radio and venues · DOLLY PARTON is the flagship modern story: she died 25 August 2026 per Rep. Tim Burchett's official statement, and only that source is in hand: research her fully in the later eras (not yours). "
 "The outline carries 128 [VERIFY] tags and 21 candidates: clear or honestly resolve each one in your eras.")
HARD["storytelling-evolution"] = ("DECISIONS #12: the through line is acting, from oral and Native performance through theatre, film, TV, games and AI performance. For eras 1-5: Native storytelling and ceremony by named nation (never generic) · Spanish religious drama in New Mexico (Los Moros y Cristianos, 1598) · colonial laws banning theatre (Massachusetts 1750, the 1774 Continental Congress resolution) and who was punished · the first professional companies · enslaved people's performance (Pinkster, parked here from holidays) · 65 [VERIFY] tags and 22 targets in the outline: clear or honestly resolve each one in your eras.")
HARD["sports-play"] = ("DECISIONS: remit widened to what children and adults do to entertain themselves, outdoor play through phones and gaming; the ADHD question is contested: named studies and real numbers only, never asserted. For eras 1-5: Native games by named nation (lacrosse among the Haudenosaunee and others, chunkey at Cahokia, the ball games' ceremonial meaning) · colonial laws against games and sports on the Sabbath and who was fined · horse racing and gambling in Virginia (who could race) · enslaved people's play and the 'holidays' · children's play and work · 69 [VERIFY] tags in the outline: clear or honestly resolve each one in your eras.")
HARD["styles"] = ("Clothing, hair, home and design trends, and what things were made of and colored. For eras 1-5: Native clothing and adornment by named nation · sumptuary laws (Massachusetts 1651) and the South Carolina Negro Act of 1740's clothing rules, with who enforced them · dyes and who grew and processed them (indigo and enslaved labor, cochineal) · the 1786 Louisiana tignon law · homespun and the boycotts · keep to this chapter's angle (fine art is art's; how materials were produced is technology's and elements').")
TASKS = [(a, b, c) for a, b, c in [tuple(x.split(":")) for x in sys.argv[1:]]] or [("T-270a", "news-communication", "1-5"), ("T-273a", "holidays", "1-5")]
for tid, slug, eras in TASKS:
    base = tid.rstrip("ab")
    path = f"control/checkpoints/{base}-{slug}.md"
    text = f"""# CHECKPOINT {base} | {slug} | full | {tid}: eras {eras}

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check {slug} --stage research
BRIEF:  control/briefs/RESEARCH.md, MODE full
MODEL:  opus
FILES:  outlines/{slug}.md · research/research-{slug}.md · workspace/{slug}.md

NOW:    (agent sets this)
NEXT:   {tid}: Unit 1.

## BURST (Jon, 2026-09-27): five agents at once

Write only your own chapter's outline, research bank, workspace file and this checkpoint. Do NOT
edit any other chapter's files: list material for them under "TO PARK" below (target chapter, era,
sourced text). The director files it after the burst.

## Measured before dispatch (2026-09-27)

{measured(slug)}

**{tid}'s job:** SEED chapter: full research of eras {eras}, one era at a time, then the bank check
for those eras. {base}b does eras 6-10 later (it may be split further).

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | research eras {eras}, one era at a time: outline + bank, clear [VERIFY], fill or honestly resolve every target and candidate in those eras | todo | |
| 2 | bank check, eras {eras} | todo | |
| 3 | final for your eras: validator, research check (the chapter passes only after its later eras) | todo | |

## SUBJECT NOTES (from the director)

{registry(slug)}

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank and the
neighbouring chapters' banks first): {HARD[slug]}

Thin eras are correct: a subject that barely existed in an early era gets a short honest cell. Never pad.

Stories: every target or candidate in your eras must become a real, named, documented person the bank
sources, or be handled honestly (never invent a name; an unnamed documented account becomes hb-zoom
prose, and the hb-story block is removed). Search `outlines/` and `manuscript/` so no other chapter
already tells the person (ignore `outlines/BOOK-OUTLINE.md`). Keep slugs unique.

## TO PARK (for the director to file after the burst)

## Sources in hand

## Gaps researched

## OPEN (should be rare)

## Outline claims left out

## Decisions and defects fixed

## Log
"""
    open(path, "w", encoding="utf-8").write(text)
    print(tid, path)
