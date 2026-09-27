# CHECKPOINT T-263 | health | full | T-263a: eras 1-5

STATUS: T-263r landed (director verified: FAIL  health / research)
VERIFY: python tools/project_state.py --check health --stage research
BRIEF:  control/briefs/RESEARCH.md, MODE full
MODEL:  opus
FILES:  outlines/health.md · research/research-health.md · workspace/health.md

NOW:    T-263r finished (Unit 3 final run). No unit in progress.
NEXT:   T-263b: full research of eras 06-10 (1800-1850 to 2000-today), one era at a time, then the bank check for 06-10.
        Insert bank era sections ABOVE the line '<!-- END OF ERA SECTIONS 01-05 (T-263a, T-263r) -->' (rename it when done).
        Seed items waiting: Elizabeth Blackwell [VERIFY 1849], FDA 1938, Medicare 1965, Tuskegee (DECISIONS #3), J. Marion Sims 1845-49 (define each procedure, policy 3b), the parked material at the bottom of the bank.
        Do not change eras 01-05. Then run project_state --check health --stage research.

## PARALLEL RUN (Jon, 2026-09-27): ten agents at once

Ten agents run at the same time, one chapter each (T-257 to T-266). **Write only your own
chapter's outline, research bank, workspace file and this checkpoint.** Do NOT edit any other
chapter's files, even to park material: list it under "TO PARK" below (target chapter, era, the
sourced text). The director files it after the batch. Reading other chapters' banks is fine.

## Measured before dispatch (2026-09-27)

FAIL  health / research
  stage=SEED eras=10/10 stories=14 (v7 c0 t7) verify_tags=5 bank=1602w outline=783w manuscript=0w validator_errors=0

**T-263a's job:** SEED chapter: full research of eras 1-5. T-263b does eras 6-10 later.

## Units

| # | unit | state | landed (note) |
|---|------|-------|---------------|
| 1 | research eras 1-5, one era at a time: outline + bank, clear [VERIFY], fill or honestly resolve every target and candidate in those eras | done | 01-02 T-263a, 03-05 T-263r. 9 verified stories, colonial-midwife target resolved as tryntje-jonas |
| 2 | bank check, eras 1-5 | done | T-263r: 4 SEARCHED NOT FOUND, 5 PATCHes (Jamestown causes, 1696-1715 smallpox, 1693 yellow fever carrier, Jack and Jackey consent, 1750-1800 actor/count notes) |
| 3 | final for your eras: validator, research check (the chapter passes only after its second half) | done | validator 0 errors. research check FAILS as expected until eras 06-10 are done |

## SUBJECT NOTES (from the director)

Registry: Health, Disease, and Medicine: Illness and healing — epidemics, doctors, hospitals, medical advances, **and public health as policy**. Not: general science (`science`); sudden calamities (`disasters`)

Hard subjects to test for actor, act, count and cause (prompts, not claims; check the bank and
the neighbouring chapters' banks first): DECISIONS #3: Tuskegee states the documented bodily course of untreated syphilis. For eras 1-5: the epidemics that killed Native people (who carried them, counts with ranges, native-nations leads the nations) · medicine in slavery (experiments on enslaved people, J. Marion Sims: define each procedure per policy 3b) · yellow fever 1793 · smallpox inoculation. Clinical words defined with method.

Stories: every target or candidate in your eras must become a real, named, documented person the
bank sources, or be handled honestly (never invent a name; an unnamed documented account becomes
hb-zoom prose, and the hb-story block is removed). Search `outlines/` and `manuscript/` so no
other chapter already tells the person (ignore `outlines/BOOK-OUTLINE.md`). Keep slugs unique.

Perishable: every 2000-today figure is dated and refreshed to 2026.

## TO PARK (FILED by the director, 2026-09-27)

RULE (coordinator, 2026-09-27, mid-T-263r): a burst started. T-263r writes ONLY health files and this checkpoint. Cross-chapter material is listed here, not filed.

- `native-nations`, era 1750-1800: Fort Pitt smallpox attempt, 24 June 1763 (Ecuyer and Trent gave Turtle's Heart and Mamaltee two blankets and a handkerchief from the smallpox hospital; Amherst's and Bouquet's July letters; effect unknowable per Fenn). Full sourced text: research/research-health.md, era 05, "Smallpox as a weapon at Fort Pitt". Not in their outline as of 2026-09-27.
- `native-nations`, era 1700-1750: Cherokee and Catawba smallpox 1738-39, 7,000-10,000 Cherokee dead (NCpedia), carriers disputed. Health era 04 bank.
- `native-nations` and `slavery-freedom`, era 1600s: Great Southeastern Smallpox Epidemic 1696-1715 spread by Indian slave raiders along trading paths (Wikipedia "Mississippian shatter zone", Kelton). Health era 03 PATCH.
- `slavery-freedom`, era 1750-1800: Doctor Caesar freed by the South Carolina Commons House (vote Nov 1749, ratified 31 May 1750, £500 to John Norman, £100 a year), his wife Lilly and daughter Hannah left enslaved, and the 1751 law barring enslaved "doctors" from giving medicine (Butler 2021, CCPL). Health era 05 bank.
- `slavery-freedom` and `war`, era 1750-1800: disease in Dunmore's Ethiopian Regiment, about 500 Black soldiers dead on Gwynn's Island 1776 (Encyclopedia Virginia, Lawler 2025). Health era 05 bank.
- `war`, era 1750-1800: Washington's order of 6 February 1777 to inoculate the Continental Army (American Battlefield Trust). Health era 05 bank.
- `city-building` or `crime-justice`, era 1750-1800: the Doctors' Riot, New York, April 1788, the Black New Yorkers' February 1788 petition about the Negroes Burial Ground, up to 20 dead, and the 1789 anatomy law (Lovejoy 2014, Smithsonian). Health era 05 bank.
- `slavery-freedom`, era 1700-1750: Onesimus's 1716 release terms (Obadiah bought as his replacement, continued unpaid work). Health era 04 bank.

## SALVAGE 2026-09-27 (T-263a killed by the usage limit, 12:50 reset)

Landed on disk (measured with git diff, committed by the director): see the Log and the
bank's T-263a PATCH headings. The agent's last NOW line was:
  T-263a Unit 1: era 03 1600s (research, then outline + bank)
**Treat that unit as possibly half-written:** check it against the outline's plan and
finish it before starting the next. Do not redo earlier units or PATCHes already in the bank.
Web search hit a quota during the batch; if search fails, use WebFetch or curl.

Pages the killed agent fetched (139; re-read the useful ones rather than searching again):
- https://www.battlefields.org/learn/articles/washington-inoculates-army
- https://www.essentialcivilwarcurriculum.com/disease-in-the-civil-war.html
- https://prss.sas.upenn.ed
- https://www.genome.gov/about-genomics/educational-resources/timelines/eugenics
- https://ehss.energy.gov/OHRE/roadmap/achre/summary.html
- https://www.academia.edu/6893396/Pre_Columbian_Tuberculosis_in_Northwest_Argentina_Skeletal_Evidence_From_Rinc%C3%B3n_Chico_21_Cemetery
- https://onlinelibrary.wiley.com/doi/10.1002/ajpa.1330510412
- https://onlinelibrary.wiley.com/doi/10.1002/ajpa.1330790305
- https://www.nature.com/articles/s41586-024-08515-5
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8901693/
- https://www.science.org/doi/10.1126/science.adw3020
- https://www.nature.com/articles/s41586-023-06965-x
- https://grokipedia.com/page/Native_American_disease_and_epidemics
- https://grokipedia.com/page/Disease_in_colonial_America
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8901693/
- https://www.nlm.nih.gov/nativevoices/timeline/index.html
- http://wsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?&amp;amp;v%3Aproject=native-people&amp;amp;sortby=DATE-asc&amp;amp;query=Era
- http://wsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?&amp;amp;v%3Aproject=native-people&amp;amp;sortby=DATE-asc&amp;amp;query=Colonizers
- http://wsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?&amp;amp;v%3Aproject=native-people&amp;amp;sortby=DATE-asc&amp;amp;query=Reshaping
- http://wsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?&amp;amp;v%3Aproject=native-people&amp;amp;sortby=DATE-asc&amp;amp;query=Defining
- http://wsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?&amp;amp;v%3Aproject=native-people&amp;amp;sortby=DATE-asc&amp;amp;query=Citizenship
- http://wsearch.nlm.nih.gov/vivisimo/cgi-bin/query-meta?&amp;amp;v%3Aproject=native-people&amp;amp;sortby=DATE-asc&amp;amp;query=Renewing
- https://www.nlm.nih.gov/nativevoices/timeline/734.html
- https://www.nlm.nih.gov/nativevoices/timeline/646.html
- https://www.nlm.nih.gov/nativevoices/timeline/673.html
- https://en.wikipedia.org/wiki/Traditional_Alaska_Native_medicine
- https://en.wikipedia.org/wiki/Medicine_man_(Native_American
- https://en.wikipedia.org/wiki/Timeline_of_First_Nations_history_in_Canada
- https://www.nlm.nih.gov/nativevoices/index.html
- https://www.nlm.nih.gov/nativevoices/interviews/theme/Healing/index.html
- https://www.nlm.nih.gov/nativevoices/interviews/index.html
- https://www.nlm.nih.gov/nativevoices/timeline/$i.html
- https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-024-08515-5
- https://journals.ametsoc.org/view/journals/eint/10/11/ei157.1.xml
- https://pmc.ncbi.nlm.nih.gov/articles/PMC1698152/
- https://www.semanticscholar.org/paper/The-demographic-collapse-of-native-peoples-of-the-Newson/b877a0b19c0ca9141f22593a58d11d807d4d018b
- https://www.thebritishacademy.ac.uk/documents/4002/81p247.pdf
- https://philpapers.org/rec/NEWTDC
- https://www.ebsco.com/research-starters/sociology/disease-and-epidemics-american-indian-communities/
- https://arxiv.org/pdf/2510.07660
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4999284/
- https://www.facebook.com/groups/584124585069376/posts/3451049735043499/
- https://www.aaas.org/news/science-submerged-skeleton-hints-first-americans
- https://www.scientificamerican.com/article/burying-bones-of-contention-native-americans-close-to-getting-ancestral-skeleton-back/
- https://stories.tamu.edu/news/2014/02/12/ancient-skeleton-proves-settlers-came-from-asia-not-europe/
- https://www.npr.org/sections/codeswitch/2016/05/05/476631934/a-long-complicated-battle-over-9-000-year-old-bones-is-finally-over
- https://www.smithsonianmag.com/history/kennewick-man-finally-freed-share-his-secrets-180952462/
- https://www.scientificamerican.com/article/indigenous-remains-do-not-belong-to-science/
- https://www.scientificamerican.com/article/ancient-bones-spark-fresh-debate-over-first-humans-in-the-americas/
- https://d.lib.msu.edu/etd/4515?q=W+P
- https://cambridge.org/core/journals/american-antiquity/article/conquistadors-excavators-or-rodents-what-damaged-the-king-site-skeletons/1583776C994B7BA505E66B9A45444DE5
- https://link.springer.com/article/10.1007/s10814-015-9084-1
- https://www.sciencedirect.com/science/article/abs/pii/S187998171200054X
- https://www.ancient-origins.net/news-history-archaeology/first-ever-evidence-ancient-bone-surgery-peru-drilled-legs-020174
- https://link.springer.com/chapter/10.1007/978-981-13-6635-2_6
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10876308/
- https://d.lib.msu.edu/etd/4515/OBJ/download
- https://d.lib.msu.edu/etd/4515/FULL_TEXT/view
- https://exeter.academia.edu/TylerCargill/Conference%20Presentations
- https://surgery.arizona.edu/blog/2022/surgery-and-native-american-medicine
- https://www.biorxiv.org/content/10.1101/051078.full.pdf
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10110152/
- https://www.medicalnewstoday.com/articles/323556
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5116069/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7546135/
- https://pubmed.ncbi.nlm.nih.gov/11788545
- https://surgery.arizona.edu/node/370
- https://pubmed.ncbi.nlm.nih.gov/12346559/
- https://www.historyoasis.com/post/facts-ancient-indigenous-medical-practices
- https://libapps.salisbury.edu/nabb-online/exhibits/show/native-americans-then-and-now/reservations/medicine-and-healing-on-native
- https://www.ebsco.com/research-starters/health-and-medicine/pre-contact-medicine-native-american-history
- https://www.legendsofamerica.com/na-medicine/
- https://www.nps.gov/afbg/learn/historyculture/medicine-wheel.htm
- https://en.wikipedia.org/wiki/Charles_Sams
- http://www.shermanindianmuseum.org/native-american-medicine.html
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2913884/
- https://www.researchgate.net/publication/11569081_Health_conditions_before_Columbus_paleopathology_of_native_North_Americans
- https://journals.sagepub.com/doi/abs/10.1177/0959683620981673
- https://onlinedigeditions.com/publication/?i=700116&p=14&pp=1&view=issueViewer
- https://www.sciencedaily.com/releases/2002/11/021101070028.htm
- https://www.scilit.com/publications/63815644b544dc58430d9d6c22078815
- https://ncbi.nlm.nih.gov/pmc/articles/PMC1071659
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10467646/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC1071659
- https://resolve.cambridge.org/core/books/the-backbone-of-history/E5EC77EDC19AA0791D2620D15DA2F49B
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1071659/
- https://encyclopediavirginia.org/entries/virginia-company-of-london/
- https://www.floridamuseum.ufl.edu/staugustine/timeline/first-contacts/
- https://viva.pressbooks.pub/amlit1/chapter/a-briefe-and-true-report-of-the-new-found-land-of-virginia-1590-waiting-on-jk/
- https://www.gutenberg.org/files/4247/4247-h/4247-h.htm
- https://docsouth.unc.edu/nc/hariot/hariot.html
- https://encyclopediavirginia.org/primary-documents/diseases-that-ravaged-indian-towns-an-excerpt-from-a-briefe-and-true-report-of-the-new-found-land-of-virginia-by-thomas-hariot-1588/
- https://en.wikipedia.org/wiki/Subversion_and_containment
- https://en.wikipedia.org/wiki/Thomas_Harriot
- https://earlyamericas.wordpress.com/anthology/thomas-hariot-from-a-briefe-and-true-report-of-the-new-found-land-of-virginia/
- https://kdhist.sitehost.iu.edu/H105-documents-web/week02/Hariot1590.html
- https://home.nps.gov/fora/learn/education/thomas-harriot-trumpet-of-roanoke.htm
- https://digitalcommons.unl.edu/zeaamericanstudies/4
- https://brewminate.com/an-overview-of-the-powhatan-chiefdom-in-17th-century-virginia/
- https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1030&context=younghistorians
- https://encyclopediavirginia.org/entries/a-briefe-and-true-report-of-the-new-found-land-of-virginia-1588/
- https://link.springer.com/article/10.1007/BF03374188
- https://scispace.com/pdf/contact-and-contagion-the-roanoke-colony-and-influenza-1vneshmkaa.pdf
- https://ncseagrant.ncsu.edu/coastwatch/wingina-wanchese-and-manteo-a-lumbee-perspective-on-the-lost-colony/
- https://encyclopediavirginia.org/entries/jamestown-settlement-early/
- https://escholarship.org/content/qt2732s9kx/qt2732s9kx.pdf
- https://idp.springer.com/authorize?response_type=cookie&client_id=springerlink&redirect_uri=https%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2FBF03374188
- https://muse.jhu.edu/pub/134/article/408431/pdf
- https://www.tshaonline.org/handbook/entries/cabeza-de-vaca-lvar-nunez
- https://www.texascounties.net/articles/discovery-of-texas/cabezadevaca-coastalnatives.htm
- https://viva.pressbooks.pub/amlit1/chapter/from-the-relation-of-alvar-nunez-cabeza-de-vaca-1542/
- https://www.sonsofdewittcolony.org/cabeza.htm
- https://courses.lumenlearning.com/suny-empire-amliterature/chapter/from-the-relation-of-alvar-nunez-cabeza-de-vaca/
- https://exhibits.library.txstate.edu/cabeza/exhibits/show/cabeza-de-vaca/relacion/la-relaci--n---p-41
- https://en.wikipedia.org/wiki/%C3%81lvar_N%C3%BA%C3%B1ez_Cabeza_de_Vaca
- https://en.wikipedia.org/wiki/Narv%C3%A1ez_expedition
- https://muse.jhu.edu/article/408431
- https://eada.lib.umd.edu/text-entries/account-of-cabeza-de-vaca/
- https://en.wikipedia.org/wiki/Adolph_Bandelier
- https://www.uwosh.edu/faculty_staff/cortes/classes/Spring2007/364/Cabeza%20de%20Vaca%20bibliografia.html
- https://www.texasbeyondhistory.net/cabeza-cooking/encounters.html
- https://www.gutenberg.org/ebooks/search/?query=cabeza+de+vaca
- https://www.gutenberg.org/ebooks/$n
- https://www.gutenberg.org/cache/epub/42841/pg42841.txt
- https://en.wikipedia.org/wiki/1616%E2%80%931619_epidemic_in_New_England
- https://en.wikipedia.org/w/api.php?action=opensearch&format=json&limit=4&search=$(python
- https://en.wikipedia.org/wiki/Samuel_Fuller_(Mayflower_physician
- https://en.wikipedia.org/wiki/Starving_Time
- https://en.wikipedia.org/wiki/The_Starving_Games
- https://en.wikipedia.org/wiki/Starving_the_Vultures
- https://en.wikipedia.org/wiki/Starting_Time
- https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srlimit=8&srsearch=
- https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles=
- https://html.duckduckgo.com/html/?q=
- https://wwwnc.cdc.gov/eid/article/16/2/09-0276_article
- http://works.bepress.com/paul_royster/7
- http://www.promedmail.org
- https://www.gutenberg.org/ebooks/search/?query=bradford+plymouth+plantation
- https://www.gutenberg.org/cache/epub/69871/pg69871.txt

## Sources in hand
- Era 01: Martin & Goodman 2002 (WJM, PMC1071659: diseases present/absent, Dickson Mounds anemia); Vagene 2022 (TB after 900 CE); Barquera 2025 Nature (treponemes American origin); Newson 1993 British Academy PDF (crowd-disease thresholds, 1492 population table).
- Era 02: Hodge 1907 Spanish Explorers (Gutenberg 42841: Cabeza de Vaca, Smith transl.; Gentleman of Elvas); Hariot 1588 (Gutenberg 4247); Encyclopedia Virginia primary doc + entry; Mires 1994 abstract (influenza, probable).

- Era 03: Bradford (Gutenberg 69871, Paget ed.); Marr & Cathey 2010 (CDC EID); Percy (Virtual Jamestown); EV Jamestown (Wolfe 2020); Blanton (Virtual Jamestown essay); Amerman 1957 (Holland Society); NYHM 1644 (Mapping Early New York); Countway + NLM (Thacher); CDC smallpox; PBS yellow fever; Bryant 2007; Salem Witch Museum 2020; Wikipedia Paspahegh, Samuel Fuller, Mississippian shatter zone.
- Era 04: MHS Feb 2021; Wikipedia 1721 outbreak and Onesimus; Paul Revere House 2020; Mass Moments (Boylston 1726 quoted); La Rue 2019 (Elizabeth Phillips); NEHS and Historic Ipswich (throat distemper, Caulfield); NCpedia Cherokee; Wikipedia 1738-39 epidemic.
- Era 05: Butler 2021 (CCPL, Caesar); Wikipedia and Mutter 2021 (Pennsylvania Hospital, 1765 school); Trent journal and d'Errico (UMass); Wikipedia Siege of Fort Pitt; ABT (Washington 1777); EV Ethiopian Regiment (Lawler 2025); Lovejoy 2014 (Doctors' Riot); Jones & Allen 1794 (Internet Archive, NLM copy, full text); O'Malley 2020; Mutter 2025 (Rush); NLM PHS (1798 act).

## Gaps researched
- T-263r bank check: de Soto as carrier and Cofitachequi origin (SEARCHED NOT FOUND, era 02); carriers of 1616-19 and 1634 (NOT FOUND, era 03); Jamestown causes (PATCH); 1693 fleet (PATCH); 1696-1715 epidemic (PATCH, added to outline); Mather bomb thrower (NOT FOUND); Jack and Jackey consent (PATCH); 1750-1800 actor and count notes (PATCH).

## OPEN (should be rare)

## Outline claims left out
- Seed 'almost no trained doctors' (1600s): no count found. Seed 'the first American medical writing' (1721): Thacher 1677/8 is older. Bridget Fuller as midwife (genealogy pages only). Boston 1677-78 death count. Fenn's 130,658 (search summary only). Rush's exact doses (search summary only). Caesar as 'first' Black medical author (search summary only).

## Decisions and defects fixed

## Log
- 2026-09-27 era 01 before-1500 DONE: outline rewritten (state thin, progress researched, no story: no named person exists), bank section '## 01' added above the parked material. Validator 0 errors.
- 2026-09-27 era 02 1500s DONE: 3 spans (Texas coast 1528-29, Cofitachequi 1540, Roanoke 1585-86) + story thomas-harriot (verified, bank-sourced). Seed span 'The Great Dying' replaced. Web search hit a session limit mid-era: de Soto-as-carrier and Cofitachequi disease origin left unsearched (see bank NOT FOUND note). Validator 0 errors.
- 2026-09-27 T-263r measured on start: eras 01-02 researched and banked; era 03 outline still seed and no era 03 bank section, so T-263a had written nothing for era 03.
- 2026-09-27 era 03 1600s DONE (T-263r): 6 spans (New England coast 1616-19, Jamestown 1607, Plymouth 1620-21, smallpox on the Connecticut River 1634, New Amsterdam midwives/surgeons/hospital, Thacher's broadside and yellow fever 1693) + stories samuel-fuller and tryntje-jonas (both verified, bank-sourced). Target colonial-midwife replaced by tryntje-jonas. Bank '## 03' added. Validator 0 errors. Sources: Bradford (Gutenberg 69871), Marr & Cathey 2010 (CDC EID), Percy (Virtual Jamestown), EV Jamestown, Amerman 1957 (Holland Society), NYHM 1644 declaration, Countway + NLM Thacher, CDC smallpox, PBS yellow fever timeline, Bryant 2007. Left out: Bridget Fuller as midwife (genealogy pages only, conflicting dates); Boston 1677-78 death count (no opened source); 'almost no trained doctors' (no count found).
- 2026-09-27 era 04 1700-1750 DONE (T-263r): 3 spans (Boston 1721 inoculation, throat distemper 1735-40, Cherokee/Catawba smallpox 1738-39 + Charleston inoculation) + stories onesimus, zabdiel-boylston (both rewritten from seed, verified, bank-sourced), elizabeth-phillips (new, ordinary, verified). Bank '## 04' added. Validator 0 errors. Seed claim 'first American medical writing' dropped (Thacher 1677/8 is older). Doctor Caesar (vote 1749, freed and printed 1750) held for era 05.
- 2026-09-27 era 05 1750-1800 DONE (T-263r): 7 spans (Doctor Caesar 1749-50, Pennsylvania Hospital 1751 + medical school 1765, Fort Pitt smallpox 1763, smallpox in the Revolution incl. Dunmore's regiment + Washington's 1777 order, Doctors' Riot 1788, yellow fever 1793, 1798 seamen's act) + stories doctor-caesar (new), benjamin-rush and jones-and-allen (rewritten from seed, verified). [VERIFY 1751] and [VERIFY 1765] cleared. Bank '## 05' added; bank end marker renamed '<!-- END OF ERA SECTIONS 01-05 (T-263a, T-263r) -->'. Validator 0 errors. Left out: Martha Ballard (home-family tells her); Fenn's 130,658 (search summary only); Rush's exact doses (search summary only); how basement patients were kept (no source).
