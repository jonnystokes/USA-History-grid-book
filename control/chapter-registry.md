# Chapter Registry — the authoritative 37-chapter list

**Updated 2026-09-06 (Jon's rulings).** The book grew from 35 to 37 chapters:
`art-music` was split into **`art`** (32) and **`music`** (33) because music is not
physical art, and **`storytelling-evolution`** (34) was added for acting and story —
which also took film out of the old art-music chapter. `styles`, `sports-play` and
`holidays` renumbered to 35/36/37; their slugs are unchanged, so nothing else moves.
`art-music` is retired — do not use that slug.

**Thin eras are correct, not a problem.** A subject that barely existed in the 1500s
gets a short honest cell (`state="thin"` or `"empty"`) with one true sentence. Never
pad a cell, and never merge unlike subjects just to avoid sparse cells — science does
not move as much in the 1500s as in the 1900s, and the grid should show that.

The spine of the book. Every outline file, research file, and grid marker keys off the **slug** (stable) — the number may change, the slug never does.

**File naming:** `outlines/<slug>.md` · `research/research-<slug>.md` · `manuscript/<slug>/`
**Every chapter** covers the same ten eras (see `grid-markers.md` §4) and follows `AGENT-BRIEF.md`.

| # | slug | Title | Part | Angle — the one lens this chapter uses | Keep out (belongs to) |
|---|------|-------|------|----------------------------------------|------------------------|
| 01 | `exploration` | Exploration and Discovery | 1 | The journeys into the unknown — who first went and found the way: land, sea, poles, deep ocean, space. | the crowds who followed (`migration`); arrival from abroad (`immigration`) |
| 02 | `native-nations` | Native Nations | 1 | Native nations as the subject — their own governments, alliances, economies, survival, and sovereignty across the whole span. | the settler journey (`migration`); war campaigns (`war`) |
| 03 | `land-environment` | Land and Environment | 1 | The land itself and Americans' changing relationship to it — use, damage, protection. | mining money (`economy`); the fuels themselves (`energy`) |
| 04 | `immigration` | Immigration to America | 2 | Arrival from other lands to stay — who came, when, from where, why, and how they were received. | the Middle Passage and forced arrival (`slavery-freedom`); movement once here (`migration`) |
| 05 | `migration` | Migration Across America | 2 | People moving and being moved across the land once here — Native movements, the trails, forced removals, the Great Migration, the Sun Belt. | who found the routes (`exploration`); arrival from abroad (`immigration`); city growth (`city-building`) |
| 06 | `city-building` | City Building | 2 | How settlements became towns and cities and how cities changed — layout, planning, water, sewers, tenements, skyscrapers, sprawl. | the move to the city (`migration`); the house itself (`home-family`); monuments (`landmarks`) |
| 07 | `home-family` | Home and Family Life | 2 | The house and the household — where Americans lived, who lived together, daily life inside. Includes housing: cabin, tenement, mortgage, suburb. | city growth (`city-building`); household appliances as inventions (`technology`) |
| 08 | `technology` | Technology | 3 | The tools and machines that changed how people lived and worked — the applied invention. | the science behind it (`science`); vehicles (`transportation`); fuels (`energy`) |
| 09 | `science` | Science | 3 | Discoveries about how the world works — knowledge and research. | applied tools (`technology`); medicine (`health`); journeys (`exploration`) |
| 10 | `energy` | Energy | 3 | What powered American life — muscle, wood, water, coal, oil, electricity, the atom, the sun. | the machines that used it (`technology`); environmental damage (`land-environment`) |
| 11 | `transportation` | Transportation | 3 | How people and goods move — trails, roads, canals, rail, cars, planes: the vehicles and systems. | the people migrating (`migration`); engine science (`science`) |
| 12 | `landmarks` | Landmarks | 3 | Notable built structures and monuments. | cities as a whole (`city-building`); houses (`home-family`) |
| 13 | `elements` | The Elements | 3 | Chemical elements as used, mined, named, and discovered in connection with the U.S. **No false firsts.** | weapons use (`war`); the cyclotron as machine (`technology`); mining money (`economy`) |
| 14 | `work-workers` | Work and Workers | 4 | What work actually felt like, and how working people organized — the daily job. | the companies (`big-business`); the whole economy (`economy`) |
| 15 | `food-farming` | Food and Farming | 4 | What Americans ate and how they grew it. | farm machinery as invention (`technology`); farm economics (`economy`) |
| 16 | `economy` | Economy | 4 | How the country makes its living — farming → industry → services; booms, panics, depressions. | currency (`money`); shops (`marketplace`); the daily job (`work-workers`) |
| 17 | `money` | Money | 4 | Money itself — coins, paper, banks, the dollar, the gold standard, the Fed, inflation. | the whole economy (`economy`); shopping (`marketplace`) |
| 18 | `marketplace` | Marketplace and Consumer Life | 4 | Buying and selling in daily life — stores, mail-order, malls, online shopping, advertising, credit, consumer culture. | money as a system (`money`); the macro economy (`economy`) |
| 19 | `big-business` | Big Business and Its Power | 4 | The scale of business **and** its clashes with government and the public — trusts, regulation, lobbying, corporate power. | the daily job (`work-workers`); the whole economy (`economy`) |
| 20 | `government-politics` | Government, Law, and Politics | 5 | How the country governs itself **and** how politics is actually practiced — Constitution, courts, laws, parties, campaigns, machines, the presidency. | rights movements (`rights-movements`); business regulation fights (`big-business`); foreign policy (`america-world`) |
| 21 | `crime-justice` | Crime, Police, and Justice | 5 | Crime, who enforced the law, and how punishment changed. | lawmaking (`government-politics`); rights campaigns (`rights-movements`) |
| 22 | `war` | War and the Military | 5 | The wars the country fought and its armed forces — plus the draft, veterans, and the civilian–military gap. | diplomacy around wars (`america-world`); the home-front economy (`economy`) |
| 23 | `america-world` | America and the World | 5 | Dealings with the rest of the world — diplomacy, alliances, treaties, empire, global influence. **Carries the territories thread** (Hawaii, Alaska, Puerto Rico, Guam, Samoa, the Philippines). | the fighting (`war`); domestic government (`government-politics`) |
| 24 | `slavery-freedom` | Slavery and Freedom | 6 | **MAJOR.** Slavery as a system and the long fight out of it — how it worked, what it did, how it ended, and **what freedom actually looked like** (full detail, not a closing paragraph). **Owns the Middle Passage.** | later civil rights campaigns (`rights-movements`, from Reconstruction's end onward) |
| 25 | `rights-movements` | Rights and Movements | 6 | **MAJOR.** Americans organizing to win rights denied them — women, civil rights, disability, LGBTQ. | slavery itself (`slavery-freedom`); the laws as laws (`government-politics`) |
| 26 | `health` | Health, Disease, and Medicine | 7 | Illness and healing — epidemics, doctors, hospitals, medical advances, **and public health as policy**. | general science (`science`); sudden calamities (`disasters`) |
| 27 | `disasters` | Disasters and Rescue | 7 | Sudden calamities and the response — fires, floods, storms, quakes, wrecks, industrial accidents, and the reforms after. | slow epidemics (`health`); war (`war`) |
| 28 | `drugs-alcohol` | Drugs and Alcohol | 7 | Intoxicants over time — alcohol and Prohibition, tobacco, other drugs, their use and control. | the law itself (`government-politics`); organized crime (`crime-justice`) |
| 29 | `religion` | Religion | 8 | Faith in America — the many religions, freedom of worship, revivals, congregations. | religious refugees arriving (`immigration`); religious holidays (`holidays`) |
| 30 | `education` | School and Education | 8 | How people learned — schools, literacy, public education, colleges, reforms. | school desegregation as a campaign (`rights-movements`) |
| 31 | `news-communication` | News and Communication | 8 | How Americans learned what was happening — messengers, the post, the press, radio, TV, the feed. | the inventions themselves (`technology`) |
| 32 | `art` | Art | 9 | The made image and the written word — painting, sculpture, photography, writing, and the artists. | music (`music`); acting, theatre and film (`storytelling-evolution`); fashion and design trends (`styles`) |
| 33 | `music` | Music | 9 | What Americans sang and played — Native traditions, psalmody, the music made under slavery, minstrelsy told plainly, folk, blues, jazz, country, gospel, rock, soul, hip-hop, streaming. **Dolly Parton (d. 25 Aug 2026) is this chapter's flagship modern story.** | the instruments as machines (`technology`); recorded-music business (`big-business`); performance as acted story (`storytelling-evolution`) |
| 34 | `storytelling-evolution` | Storytelling Evolution | 9 | People acting out stories, from oral and Native performance traditions through theatre, minstrel and vaudeville stages, silent film, radio drama, television, New Hollywood, video games, and AI-generated performance. Named this rather than "Film" because early filmed drama was a recorded stage play — the through line is the acting, not the technology. | the songs themselves (`music`); the cameras and consoles as machines (`technology`); the studio business (`big-business`) |
| 35 | `styles` | Styles | 9 | Changing tastes — clothing, hair, home and design trends, **and what things were made of and colored** (absorbed from the old Materials and Colors). | fine art (`art`); how materials were produced (`technology`/`elements`) |
| 36 | `sports-play` | Sports and Play | 9 | How Americans and their children entertained themselves and how it changed — unstructured outdoor play, games, teams, what sport came to mean, arcades and consoles, and the shift to phones and online play. | holidays (`holidays`) |
| 37 | `holidays` | Holidays | 9 | American holidays and celebrations — how the country marks its days and how that changed. | sports (`sports-play`); religion itself (`religion`) |

**Afterword (not a grid chapter, no eras):** `how-we-know` — how history is checked, the Thanksgiving and frontier myths, the Lost Cause, monuments, and why this book cites sources.

## Parts
1. The Land and Its First Peoples (01–03) · 2. Coming, Moving, Settling (04–07) · 3. Making and Building (08–13) · 4. Work, Food, and Money (14–19) · 5. Power, Law, and War (20–23) · 6. Freedom and Fairness (24–25) · 7. Health and Safety (26–28) · 8. Faith, Learning, and News (29–31) · 9. Culture and Play (32–37)

## Director rulings (2026-07-23 — agents follow these)

1. **Kossola / the *Clotilda* belongs to `slavery-freedom`** (the last slave ship, the Middle Passage, Africatown). `immigration` hands off in one sentence. Immigration is not short of stories — it keeps Annie Moore, Carl Schurz, Lee Puey You, the 1654 Jewish refugees, and Tung Trinh, and should still add more voluntary-arrival lives.
2. **The domestic slave trade is told in BOTH** — that is the grid working. `slavery-freedom` leads: people as property, families broken by sale, what it did. `migration` tells it as a forced journey: routes, coffles, ships, numbers, conditions. Neither repeats the other.
3. **Boundary rule settles all date conflicts** — an event sits in the era containing its date. So: Beckwourth Pass (1850) → 1850–1900 · Amelia Stewart Knight (1853) → 1850–1900 · Conrad Reed's nugget (1799) → 1750–1800, the mining that followed (1803) → 1800–1850 · the Cascadia earthquake (Jan 1700) → 1700–1750 · Lewis Hine's photographs (1908–12) → 1900–1950, with the practice's peak noted in 1850–1900.
4. **Boarding schools:** `native-nations` leads (what was done to the nations and how they endured); `education` covers them as part of the schooling system. Agent's placement was right.
5. **`home-family` is allowed to be short on famous names.** It is the ordinary-lives chapter by nature — do not force celebrities into it. Its strength is documented everyday people.
7. **THE SCHOOL SYSTEM — Jon's explicit must-have (2026-07-23).** All of the following has to land somewhere, and none of it may be dropped. `education` carries the spine; the others take their own angle:
   - **`education` (30) — the core:** the one-room schoolhouse and what a school day was actually like · **discipline and punishment** (the switch, the dunce cap, the hickory stick, "spare the rod," and how and when corporal punishment ended) · dame schools and academies · the common-school movement · public vs. **private** vs. **parochial** vs. **charter** (from 1991) vs. **magnet** schools · **homeschooling** (its legality fight and modern growth) · the rise of the high school · teachers as a profession (and how it became women's work) · curriculum, textbooks, testing.
   - **`religion` (29):** religious instruction in schools, parochial school systems, Bible reading and prayer, the court rulings that ended school prayer, and religious objections to curriculum.
   - **`native-nations` (02):** Indian boarding schools — Carlisle, "kill the Indian, save the man," language suppression, and the survivors.
   - **`rights-movements` (25):** girls' and women's access to schooling, Title IX, school desegregation as a *campaign*, and disability access to schools.
   - **`slavery-freedom` (24):** anti-literacy laws that made teaching enslaved people a crime, and the Freedmen's schools built the moment freedom came.
   - **`government-politics` (20):** school law, funding fights, and the major court cases as law.
   - **`home-family` (07):** children's daily routine, chores vs. school, and homeschooling as household life.
8. **`immigration` gets more stories.** Jon approved expanding it. Add verified voluntary-arrival lives across eras — a colonial-era arrival, an Irish or German famine-wave arrival, a Southern/Eastern European Ellis Island arrival, a post-1965 arrival, and a recent one. Famous names first, then ordinary lives.
9. **`research-ch17-prejudice.md` splits three ways** — slavery material → `research-slavery-freedom.md`; women/civil rights/disability/LGBTQ → `research-rights-movements.md`; the Radium Girls' fight → also `work-workers` and `health`. Do this split when `slavery-freedom` is researched.

## Existing research banks — RENAMED to slug names (done 2026-08-07)
All live banks now use `research/research-<slug>.md`. One legacy exception: `research-ch17-prejudice.md` stays under its old name until the `slavery-freedom` research agent splits it three ways (ruling 9). Historical mapping (for reading old notes):
`research-ch01-exploration`→`exploration` · `ch02-immigration`→`immigration` · `ch03-migration-west`→`migration` · `ch04-city-development`→`city-building` · `ch05-technology`→`technology` · `ch06-science`→`science` · `ch07-transportation`→`transportation` · `ch08-landmarks`→`landmarks` · `ch09-economy`→`economy` · `ch14-government-and-law`→`government-politics` · `ch15-war`→`war` · `ch17-prejudice`→ splits between `slavery-freedom` and `rights-movements` · `ch18-health`→`health` · `ch27-elements`→`elements`
