# CHECKPOINT T-234 | city-building | prose (v2 revision) | all 10 eras, 3 part files

<!-- The director fills the header and the unit list before dispatch. The agent keeps
     everything else current, and commits and pushes after every unit. Write it for a
     stranger who has only this file and the repo. -->

STATUS: IN-FLIGHT
VERIFY: python tools/project_state.py --check city-building --stage prose
        (per part: python tools/project_state.py --punct manuscript/city-building/<part>.md)
BRIEF:  standard REVISION brief (control/RESUME.md) + cloud lines (control/CLOUD-WORKFLOW.md §5)
FILES:  manuscript/city-building/part1-before-1800.md · part2-1800s.md · part3-1900s-and-today.md
        (read-only sources: outlines/city-building.md · research/research-city-building.md)
PLAN:   one agent per part file. T-234a = part 1, T-234b = part 2, T-234c = part 3.
MODEL:  native-nations (T-233) is the finished v2 example. Its three parts show the voice.

NOW:    T-234c landed units 8-9 (eras 1900-1950, 1950-2000). Working on unit 10 (era 2000-today).
NEXT:   part 3, era 2000-today, then whole-file self-review.

## Baseline before revision (measured 2026-09-26)

| part | prose words | em dashes | semicolons |
|---|---|---|---|
| part1-before-1800.md | 3,810 | 12 | 5 |
| part2-1800s.md | 4,238 | 23 | 6 |
| part3-1900s-and-today.md | 5,720 | 48 | 12 |

A large drop in words after revision is a warning sign of lost facts. The director compares.

## Units

| # | unit | state | landed (commit / note) |
|---|------|-------|------------------------|
| 1 | part1 era before-1500 | landed | v2 revision, T-234a |
| 2 | part1 era 1500s | landed | v2 revision, T-234a |
| 3 | part1 era 1600s | landed | v2 revision, T-234a |
| 4 | part1 era 1700-1750 | landed | v2 revision, T-234a |
| 5 | part1 era 1750-1800 | landed | v2 revision, T-234a, plus whole-file self-review |
| 6 | part2 era 1800-1850 | landed | v2 revision, T-234b |
| 7 | part2 era 1850-1900 | landed | v2 revision, T-234b, plus whole-file self-review |
| 8 | part3 era 1900-1950 | landed | v2 revision, T-234c |
| 9 | part3 era 1950-2000 | landed | v2 revision, T-234c |
| 10 | part3 era 2000-today | todo | |

<!-- state: todo | working | landed | skipped (say why) -->

## Facts taken from the research bank

<!-- Fact, bank section, and the sentence it went into. -->

- (none taken for eras before-1500, 1500s)
- 1600s, bank "Fort towns" (MAAP/Columbia): Paulo d'Angola, Simon Congo and Anthony Portuguese are named as men who DUG the 1653 trench. The prose had named them only as 1644 half-freedom grantees and implied the link. Now stated.
- 1600s, bank "Fort towns": the 1644 grant's words "at present born or yet to be born", now quoted for the children. "North River" glossed as the Hudson (MAAP: "to the Hudson River"). Wall "reported complete" (bank) replaces "reported standing".
- 1600s, bank "Fort towns": Boston cow-path legend source named as Boston Magazine, 2018. Boston PD history pages as source for the watch as the start of the police.
- 1750-1800, bank "The land the capital was built on": Residence Act SIGNED July 16, 1790 (prose had "Congress passed" on that date, an institution-as-actor and a date error). Washington "rode" the country. Nameroughquena (west bank of the Potomac, opposite Theodore Roosevelt Island) and a third unnamed town on a northwest bluff, added to the three Native towns. The 245 figure attributed to the Smithsonian NMAAHC (whose site was part of Young's plantation), 260 to Histories of the National Mall (George Mason Univ.).
- 1750-1800, bank "L'Enfant": the Residence Act let the President appoint three commissioners (used to define "commissioners").
- 1750-1800, bank "Banneker": Silvio Bedini, the NPS and the Library of Congress named as the historians crediting Banneker with the boundary astronomy.
- 1750-1800, bank "Philadelphia's waterworks": 20,000 "fled" (prose had "left").
- 1800-1850, bank "Rochester": 1830 census figure 9,269 (prose had "about 9,200"). 12,630 dated to 1834, "the charter year" (prose had "mid-1830s"), now "By 1834, the year Rochester became a city". The prose's "fifteen years" became "more than eight times as many as in 1820" (1820 to 1834 is fourteen years, so "fifteen" was wrong).
- 1850-1900, bank "Raising Chicago": the 1860 Lake Street raisers are a "consortium of engineers including George Pullman" (prose had "contractors"). Now "engineers".
- 1850-1900, bank "Tenements": the 1901 law also "outlawed the dumbbell" and required courtyards (prose had only "real light, real air, indoor toilets, fire protection"). Now stated.
- 1850-1900, bank "Mohawk ironworkers": the NMAI exhibition's towers (Empire State, Chrysler, George Washington Bridge, World Trade Center) replace "runs forward through the towers of the next century".
- 1850-1900, bank "White City": "seeded the City Beautiful movement", now "Planners in the next era built on that idea in what they called the City Beautiful movement".
- 1800-1850, bank "San Francisco": growth placed "during the California Gold Rush" (bank: Gold Rush references, "migration leads the rush").
- 1900-1950, bank "Oak Ridge and the secret cities": the removals now stated in full (about 1,000 families; Wheat, Elza, Scarboro/Scarborough, Robertsville, New Bethel, New Hope; 3,000 to 4,000 people as a range, Tennessee Encyclopedia named; October 1942, Army Corps of Engineers, declaration of taking under eminent domain, about 59,000 acres at $46.86 an acre; notices nailed to fence posts; a few weeks; gone within a year; most accepted, a few sued; an eighth of Roane County, a seventh of Anderson County). Eminent domain is now defined here at first use.
- 1900-1950, bank "Chicago River reversal": the Sanitary District of Chicago named as the body whose engineers did the reversal (prose had "The engineers' answer").
- 1900-1950, bank "The race to the sky": the official Chrysler height credited to the Council on Tall Buildings and Urban Habitat (CTBUH). Mohawk crews' towers named as the Empire State and Chrysler buildings (NMAI "Booming Out"). Empire State "half empty" (bank "half-empty") replaces "much of it stood empty".
- 1900-1950, bank "Burnham": "much of" the lakefront's openness traces to the plan (prose said the whole open lakefront did, stronger than the bank).
- 1900-1950, bank "Oak Ridge / Colleen Black": trailer camp (prose had "the government's instant housing"); TV appearances on NBC Nightly News and the History Channel replace the unsourced superlative "one of the most recorded voices".
- 1950-2000, bank "Urban renewal": sources named for the figures (Brent Cebul, Boston Review 2020, and the Digital Scholarship Lab's "Renewing Inequality" project).
- 1950-2000, bank "Jacobs vs. Moses": Jacobs led (bank "chaired") the Joint Committee to Stop the Lower Manhattan Expressway; the riot charges were later reduced; Caro's Pulitzer dated 1975 (prose implied 1974).
- 1950-2000, bank "Rondo": the four moved buildings stand on the University of Minnesota's St. Paul campus (prose had "a University of Minnesota campus").

## Decisions and known gaps

<!-- Rule conflicts settled, and how. Defects beyond style found and fixed (these go to
     AUDIT-QUEUE). Anything a successor must not undo. -->

- before-1500: the Chaco paragraph said "Those two dates measure different things" before the 1140s date had appeared (information-order defect, reads as a contradiction). Fixed: each date now says what it measures. Keep "prehistoric" on Monks Mound (bank flag 14).
- before-1500: "Four Corners country" defined as where Colorado, Utah, Arizona and New Mexico meet. This is a plain-geography definition, not from the bank.
- 1500s: era summary was metadiscourse plus a fragment triad. Rewritten as facts. Laws of the Indies imperatives recast as "had to" statements (no quotation, so no wording to keep). "Among the first" claim attributed to writers on town-planning history (bank: ArchDaily, scholarly literature).
- 1600s: "American town-builders copied it for the next two hundred years" is in the outline but NOT in the bank. Kept (no fact may leave), flagged for AUDIT-QUEUE.
- 1600s: the bank has nothing on which Native nations lived on the sites of Jamestown, Boston, New Amsterdam or Philadelphia, so the prose cannot name them. "Before the settlers arrived" now reads "before the English settlers arrived" so it does not imply empty land. Gap for AUDIT-QUEUE (land-erasure watch).
- 1600s: Wall paragraphs reordered so the workers stay the subject and the name of Wall Street comes first. Closing lines "The wall is long gone..." and "Nobody decided Boston's streets. Somebody decided Philadelphia's..." (antithesis, closing reversal) removed, their facts moved into earlier sentences.
- 1700-1750: span label "Fire, the city killer" personifies fire, but marker lines are frozen by the brief. Left as is, flagged for AUDIT-QUEUE.
- 1750-1800: era summary and span no longer withhold names ("a French-born engineer ... a free Black farmer" now L'Enfant, Ellicott, Banneker). "Washington looks like no other American city" cut as an unsourced superlative; the two-street-system fact kept. "workmen moved his body" became a passive: the bank says only "reinterred", with no actor. Closing moral "The idea lasted..." cut, and its fact kept as a plain sentence. Native deaths "in wars": the NPS page does not say who fought, and the prose says so. Tobacco "inspection house" glossed from the term itself, not from the bank.
- 1800-1850: LAND ERASURE fixed. Era summary said San Francisco had been "a stretch of empty coast"; the bank has about 200 people there in 1846. Now "a small coastal settlement". The bank names no Native nation at Rochester, Chicago, San Francisco or Manhattan, so the prose cannot name them. Gap for AUDIT-QUEUE.
- 1800-1850: claims in the prose NOT in the bank, kept and flagged for AUDIT-QUEUE: Chicago settled where "a short river met Lake Michigan"; cholera's bodily course (definition); "no piped water", wells beside privies; Randel's marker "at every corner of every future crossing"; Strong could "turn a tap" and "almost nobody in an American city" could bathe at home before; wheat in / flour out by canal.
- 1800-1850: "The men governing New York" decided on the Croton water: the bank names no official, so the prose says "New York's leaders" and names Jervis as the only person the records give. Strong's quotation split at its em dash with no word changed. Strong's closing lines ("That is the whole change in one household...") cut as a closing reversal; their facts (41 miles, parade) stand in the span. "While the water came nearer his part of town" became "while the water was still on its way" (the quotation itself says it was flowing towards the city).
- 1850-1900: marasmus. Bank word is "severe malnutrition"; prose said "starvation". Kept both: "severe malnutrition, a form of starvation". Recorded here as a word-strength difference.
- 1850-1900: Riis "then the city's police commissioner" implied Roosevelt held the post in 1890. The bank gives no year, so now "as New York City's police commissioner". Riis book spurred the "first significant" (now "first major") tenement laws, while the span calls the 1879 Act the first tenement rules: both kept, the tension is for AUDIT-QUEUE. The bank does not support "first" for the 1879 Act.
- 1850-1900: LAND RUN. "The ground thrown open that day was Native land, taken from the nations who held it" (agentless, "thrown open"). The bank does not name the nations or the people who took the land, so the prose now says the research does not identify them. Gap for AUDIT-QUEUE. Seneca Village: the bank names no official who took the land. Prose says so.
- 1850-1900: claims in the prose NOT in the bank, kept and flagged for AUDIT-QUEUE: sewers "had no pumps"; "several feet" of fill; customers buying while the floor rose; Otis stood on the platform; top floors cheapest before elevators, dearest after; White City "built to last one season", "millions of visitors", the idea visitors took away; tenement landlords housed "most" of the arriving poor and "for decades" no law required anything; Riis worked nights, cellars at a few cents; owner sealed 97 Orchard (bank passive); Joseph Moore an Irish immigrant (bank says Bridget); all of the Olmsted body except the 1858 win and 1893 site plan (farmer, journalist, never designed a park, landscape architecture profession, Prospect Park, Emerald Necklace, dozens of places, the made-countryside argument, cities expected parks after him); Guthrie "surveying, laying out lots"; colonial towns "took years".
- 1850-1900: closing lines cut or recast: "What he had demonstrated was..." (Riis, moved to the front), "The Moores are the ones the records let us name" (false: other residents are named), "Central Park exists... Both of those are the record" (facts folded into the taking), "Cities in the Northeast were raised in part by..." (moved to the front). Labels revised: "Chicago lifts itself out of the mud" (city as actor), "Central Park, and what stood there first" (Seneca Village was not first), "Out: streetcars stretch the city" (vehicles as actor). "lift the entire downtown into the air" became raising the downtown buildings to the new street level (precision).
- 1700-1750: "London ... hundreds of thousands" and "volunteer fire companies ... for the next hundred years" are in the outline/prose, not in the bank. Kept, flagged for AUDIT-QUEUE.
- 1900-1950: LAND ERASURE FIXED (bank flag 16). The prose still read "on empty ridgeland" and the era summary "on empty ground"; the span label read "Secret cities from nothing". All three now state the removals (label: "Oak Ridge: a secret city on taken farmland"). The bank names no removals at Los Alamos or Hanford/Richland, so the prose says nothing about who was on that land. Gap for AUDIT-QUEUE (land-erasure watch).
- 1900-1950: the Oak Ridge eviction notices are a bank passive with no actor. Prose says the sources do not say who put them up.
- 1900-1950: era summary said the covenant-bound "arrivals", immigrants included, were packed into a few districts. The covenants in the bank bar Black buyers (sometimes Jewish or Asian). Now the summary says Black families. Precision fix.
- 1900-1950: labels revised: "The river turned around" (river as actor) now "Drinking water for Chicago and San Francisco"; "Zoning" em dash to colon; "The race to the sky" now "The contest for the tallest building"; "Where the Great Migration settled" (migration as actor) now "Where Great Migration families could live".
- 1900-1950: closing lines cut: "What the city got was a water supply it had not had before" (restated), "The building was the argument made visible, not the trigger" (now "Supporters of the resolution used the building as their best-known example", bank "poster child"), "and they did" (zoning), "The plans themselves are the record" (Burnham), "The lines outlived the agency" (redlining).
- 1900-1950: definitions not from the bank, glossed from the plain meaning of the term: the Depression ("the years of the 1930s when many businesses failed and many people lost their work"), low-to-moderate income, majority-minority, conservationists, hotplate, asbestos ("a mineral fiber"), contractor, weld, ironworker, water mains, storm lines. "American forces dropped an atomic bomb on Hiroshima, in Japan" replaces the agentless "the bomb was dropped on Hiroshima": the actor is from general knowledge, not the bank.
- 1900-1950: claims in the prose NOT in the bank, kept and flagged for AUDIT-QUEUE: immigrants among the arrivals; "Anyone who owned a lot could build almost anything"; Equitable's shadow over "whole blocks"; Jason Barr named (bank names only "Building the Skyline"); "nearly every American city" adopted zoning (bank: "spread nationwide"); zoning used to exclude by race or income (bank has it only as a flag line); people in other cities expecting a plan after 1909; Van Alen "did not want them to know"; Mohawk trade "passed down ever since"; each later owner bound by a covenant; "block by block"; lenders across the country used the HOLC grades "for decades" (bank credits FHA underwriting, not lenders using HOLC maps); well-built houses on quiet streets graded red; "cement and asbestos" panels (bank: "cemesto"); shops at Oak Ridge; "almost none" of the residents told; helium mechanism, "miles of pipe", workers not allowed to ask, the plant "separating" (Colleen Black).
- 1950-2000: FALSE ATTRIBUTION fixed. The era summary put "at least 300,000 families" on both programs (urban renewal and highways). The bank gives that floor for urban renewal only. Now attached to the 1949 housing law alone.
- 1950-2000: FALSE FIGURE fixed. "Some old downtowns lost more than half their people": the figures are for whole cities, and Detroit fell 48.6 percent (1,849,568 to 951,270), not more than half. Now "St. Louis lost about 60 percent of its people, and Detroit lost nearly half".
- 1950-2000: SELF-CONTRADICTION found, not settled. Marvin Roger Anderson was "eight" when the news came in 1958 and "approaching 83" in March 2022 (born about 1939). The two cannot both be true. The bank note claims they compute, and they do not. The prose now states both, attributed to Sahan Journal, and says the sources do not settle which is right. The record line now reads "His family learned of the freeway in 1958", with no age. For AUDIT-QUEUE.
- 1950-2000: Stokes story said Hatcher "won the same office" in Gary. He won Gary's mayoralty, not Cleveland's. Fixed. "Same night" now "same day" (bank).
- 1950-2000: Rondo "the case with the fullest record" (a superlative the bank does not make, bank: "documented case") now "one well-documented case". The Rondo route: the bank names no official who chose it, and the prose says so.
- 1950-2000: closing lines cut or recast: "The money to buy a house was there in one place and not in the other, because people wrote rules that put it there"; "the range is what the sources support"; "The argument is not settled" (now "Historians have not settled that argument"); "they were the plan" (em-dash pivot); "The people running cities still do both things" (moved up into the Jacobs paragraph, kept as a claim). Labels revised: "Urban renewal, and what the word covered" now "Urban renewal: clearing neighborhoods for developers"; "Sprawl, and the emptying middle" now "Sprawl, and the people who left the old centers"; "The Sun Belt boom" now "Growth in the Sun Belt".
- 1950-2000: definitions not from the bank, glossed from the plain meaning of the term: metropolitan area, subdivision, insured mortgage, underwriting rules, expressway, inciting to riot, public housing, annexation (reworded), State Law Librarian.
- 1950-2000: claims in the prose NOT in the bank, kept and flagged for AUDIT-QUEUE: the engineers' "two reasons" for routing freeways through Black and poor neighborhoods; the Title I write-down (federal officials paid the difference); blockbusting; FHA-insured suburban mortgages and underwriting refusals (bank has FHA only as a flag line, "standard scholarship", Rothstein 2017); "builders at the edge of every metropolitan area" copied Levittown; the mass-production description; Jacobs "had no training in planning" and the content of her argument; planning schools teaching her book; "most people who know Moses's name learned it from that book"; city officials today doing both kinds of work; Rondo Days' purpose; businesses on the proposed land bridge; "oil slick and floating trash" on the Cuyahoga; Stokes's demand as a call for the water-pollution laws; "dozens" of Black mayors in the 1970s and 1980s; separate suburbs not forming around annexing cities; Sun Belt cities laid out for cars with no older walking city.

## Log

<!-- One line per save: date-time | unit | what landed | validator result | --punct result -->

- 2026-09-26 | 1 before-1500 | era revised to v2 | 0 errors | era clean (file still has later-era marks)
- 2026-09-26 | 2 1500s | era revised to v2 | 0 errors | era clean
- 2026-09-26 | 3 1600s | era revised to v2 | 0 errors | era clean
- 2026-09-26 | 4 1700-1750 | era revised to v2 | 0 errors | era clean
- 2026-09-26 | 5 1750-1800 + whole-file self-review | revised to v2 | 0 errors | emdash=0 semicolon=0
- 2026-09-26 | 6 1800-1850 | era revised to v2 (T-234b) | 0 errors | era clean (file still has era-07 marks: emdash=16 semicolon=6)
- 2026-09-26 | 7 1850-1900 + whole-file self-review | revised to v2 (T-234b) | 0 errors | emdash=0 semicolon=0
- 2026-09-26 | 8 1900-1950 | era revised to v2 (T-234c) | 0 errors | era clean (file still has later-era marks: emdash=30 semicolon=9)
- 2026-09-26 | 9 1950-2000 | era revised to v2 (T-234c) | 0 errors | era clean (file still has era-10 marks: emdash=13 semicolon=1)
