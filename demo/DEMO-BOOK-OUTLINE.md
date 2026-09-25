<!-- hb-note -->
**DEMO BOOK — throwaway test data to exercise the grid HTML viewer. NOT part of the 35-chapter book.**

**What this is:** a tiny three-lens demo of the grid format (v3). It exists only so a viewer program has real, finished `mode="prose"` content to render, with every feature turned on: empty cells, thin cells, full cells, stories with and without films, `famous` and `ordinary` people, and cells where the narration zooms in to a story and back out again.

**The product this viewer should present:** a live grid you move through in three ways.
- **Scroll DOWN through time:** ten eras, from Before 1500 down to 2000 to Today, always in the same order.
- **Slide LEFT and RIGHT through lenses:** three chapters looking at the same ten eras from three different angles — Spooky America, Sweet Tooth, and Thinking Machines. The same era sits side by side across all three.
- **ZOOM IN from era to story:** each cell opens wide (the whole era), may step to a shorter span (a decade, a movement, a single film), and closes in on one true story about a real person. The narrator can pull back out and dive in again.

**Shading the grid:** cells carry `state` (did the subject exist here — empty / thin / full) and `progress` (how finished — here always `written`). The Thinking Machines lens deliberately shows empty and thin cells; Spooky America is full in every era because fear is timeless.

**For the viewer AI:** strip every hb-note block (like this one) from the reader view. Below are the three chapter files in order: 01 Spooky America, 02 Sweet Tooth, 03 Thinking Machines. Each begins with its own hb-chapter line and holds ten hb-time sections.
<!-- /hb-note -->



<!-- hb-chapter id="01" slug="spooky-america" title="Spooky America" part="1" mode="prose" -->

# Chapter 1: Spooky America

<!-- hb-note -->
**DEMO CHAPTER — throwaway test data, not part of the 35-chapter book.**
**Angle:** the monsters, witches, ghosts, and things Americans have feared, era by era.
**Why it fills every cell:** fear is timeless, so every era here is `state="full"`.
This block is editor-only and is never shown to a reader; the final parser deletes every hb-note block.
<!-- /hb-note -->

<!-- hb-time:start id="before-1500" order="01" chapter="spooky-america" label="Before 1500" state="full" progress="written" -->
## Before 1500
<!-- hb-zoom level="era" -->
Long before ships came from across the ocean, the many nations of this land already told stories in the dark to explain the world and to name what should be feared. Storms, sickness, and the deep woods all had shapes in these stories, and the shapes were old.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="the Thunderbird" -->
One of the best known is the Thunderbird, a giant bird told of by many peoples, from the Plains to the Pacific coast. Its beating wings were said to make the thunder, and the flash of its eyes the lightning, so that a summer storm was a living thing passing overhead.
<!-- /hb-zoom -->
<!-- hb-time:end id="before-1500" -->

<!-- hb-time:start id="1500s" order="02" chapter="spooky-america" label="The 1500s" state="full" progress="written" -->
## The 1500s
<!-- hb-zoom level="era" -->
As the first Spanish settlers pushed into the Southwest, they carried their own fears with them, and a world where the Devil, witches, and restless spirits were treated as plain fact.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="La Llorona" -->
With them traveled the tale of La Llorona, the Weeping Woman: a mother who drowned her children and now wanders rivers and ditches at night, crying for them. Parents told it to keep children away from the water after dark, and it took root in the Southwest, where it is still told today.
<!-- /hb-zoom -->
<!-- hb-time:end id="1500s" -->

<!-- hb-time:start id="1600s" order="03" chapter="spooky-america" label="The 1600s" state="full" progress="written" -->
## The 1600s
<!-- hb-zoom level="era" -->
The Puritans of New England believed the Devil was real, close, and working through their neighbors. That belief reached its most famous and deadly peak at the century's end.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="the Salem witch trials" -->
In 1692, in Salem, Massachusetts, a group of girls began to accuse their neighbors of witchcraft. Before the panic ended, more than two hundred people had been accused and twenty were put to death.
<!-- /hb-zoom -->
<!-- hb-story:start slug="tituba" name="Tituba" movie="" kind="ordinary" status="verified" -->
### Tituba

> **Who:** An enslaved woman in the Salem household of Reverend Samuel Parris, among the very first three people accused.
> **When and where:** Salem, Massachusetts, 1692.

Tituba was one of the first three women accused when the Salem panic began. Under questioning she confessed, describing the Devil and a book of witches, and her words helped set the whole terrible machine in motion. She survived the trials, but almost nothing certain is known of what became of her afterward.
<!-- hb-story:end slug="tituba" -->
<!-- hb-time:end id="1600s" -->

<!-- hb-time:start id="1700-1750" order="04" chapter="spooky-america" label="1700 to 1750" state="full" progress="written" -->
## 1700 to 1750
<!-- hb-zoom level="era" -->
The old fear of the Devil did not fade with the new century. In the colonies, sermons still warned of him, and the wild, half-settled land bred new local legends of its own.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="the Jersey Devil" -->
The most enduring came out of the New Jersey Pine Barrens: the Jersey Devil, said to have been born in 1735 as the thirteenth child of a woman known only as Mother Leeds. In the telling, the child turned into a winged, hoofed creature and flew off into the pines, where people have claimed to see it ever since.
<!-- /hb-zoom -->
<!-- hb-time:end id="1700-1750" -->

<!-- hb-time:start id="1750-1800" order="05" chapter="spooky-america" label="1750 to 1800" state="full" progress="written" -->
## 1750 to 1800
<!-- hb-zoom level="era" -->
As the colonies became a country, ghost stories were part of everyday life. Old houses, lonely roads, and country graveyards all had their haunts, passed along at the fireside on winter nights.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="New England ghost lore" -->
New England was especially thick with such tales. Every town seemed to have a haunted lane or a house no one would buy, and the stories were told as neighborhood news as much as entertainment.
<!-- /hb-zoom -->
<!-- hb-time:end id="1750-1800" -->

<!-- hb-time:start id="1800-1850" order="06" chapter="spooky-america" label="1800 to 1850" state="full" progress="written" -->
## 1800 to 1850
<!-- hb-zoom level="era" -->
In the new century, American writers turned the country's fears into stories on the page, and gave the young nation its first homegrown monsters and ghosts.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="the Headless Horseman" -->
In 1820, Washington Irving published "The Legend of Sleepy Hollow," and gave America one of its lasting ghosts: the Headless Horseman, a phantom rider searching the night for the head he lost in war.
<!-- /hb-zoom -->
<!-- hb-story:start slug="edgar-allan-poe" name="Edgar Allan Poe" movie="" kind="famous" status="verified" -->
### Edgar Allan Poe

> **Who:** The American writer who became the master of the horror and mystery tale.
> **When and where:** Lived 1809 to 1849, mostly along the East Coast.

Edgar Allan Poe filled his tales with beating hearts under the floorboards, bodies behind brick walls, and a raven that would only say one word. More than anyone, he taught American readers to enjoy being frightened, and horror writers have been following him ever since.
<!-- hb-story:end slug="edgar-allan-poe" -->
<!-- hb-time:end id="1800-1850" -->

<!-- hb-time:start id="1850-1900" order="07" chapter="spooky-america" label="1850 to 1900" state="full" progress="written" -->
## 1850 to 1900
<!-- hb-zoom level="era" -->
In the second half of the century, Americans became fascinated with talking to the dead. A whole movement called Spiritualism grew up around the idea that the living could reach the spirits of the departed.
<!-- /hb-zoom -->
<!-- hb-story:start slug="fox-sisters" name="The Fox Sisters" movie="" kind="ordinary" status="verified" -->
### The Fox Sisters

> **Who:** Two young sisters whose "spirit rappings" helped launch Spiritualism.
> **When and where:** Hydesville, New York, starting in 1848.

Kate and Margaret Fox claimed that mysterious rapping sounds in their home were messages from a spirit. Their fame helped set off a craze for séances that swept the country for decades. Years later, Margaret publicly confessed the raps had been a trick made with the joints of her toes, though by then many believers refused to let the idea go.
<!-- hb-story:end slug="fox-sisters" -->
<!-- hb-zoom level="span" label="the Ouija board" -->
The hunger to reach the other side turned into a product anyone could buy. In 1890 the Ouija board went on sale as a parlor game, promising to spell out messages from the beyond on a rainy evening at home.
<!-- /hb-zoom -->
<!-- hb-story:start slug="lizzie-borden" name="Lizzie Borden" movie="" kind="famous" status="verified" -->
### Lizzie Borden

> **Who:** A woman tried for the axe murders of her father and stepmother in a case that gripped the nation.
> **When and where:** Fall River, Massachusetts, 1892.

In 1892, Andrew and Abby Borden were killed with a hatchet in their own home, and Andrew's daughter Lizzie was charged with the crime. A jury found her not guilty, but the public never quite made up its mind, and a grim schoolyard rhyme kept her name spooky for more than a century.
<!-- hb-story:end slug="lizzie-borden" -->
<!-- hb-time:end id="1850-1900" -->

<!-- hb-time:start id="1900-1950" order="08" chapter="spooky-america" label="1900 to 1950" state="full" progress="written" -->
## 1900 to 1950
<!-- hb-zoom level="era" -->
The first half of the new century turned American fear into a business, projected onto movie screens and broadcast over the radio into millions of homes at once. This is where the monsters became stars.
<!-- /hb-zoom -->
<!-- hb-story:start slug="harry-houdini" name="Harry Houdini" movie="" kind="famous" status="verified" -->
### Harry Houdini

> **Who:** The world-famous escape artist who spent his last years exposing fake mediums.
> **When and where:** Across the United States in the 1920s.

By the 1920s the séance craze was still going strong, and Harry Houdini set out to prove how much of it was fraud. Using his own showman's knowledge of tricks, he attended séances in disguise and revealed how the "spirits" tipped tables and made noises in the dark.
<!-- hb-story:end slug="harry-houdini" -->
<!-- a new era-level zoom after a story = the narrator pulling back to the wide view before the movie monsters -->
<!-- hb-zoom level="span" label="Universal's monsters" -->
Then Hollywood gave the fears a face. In a single year, 1931, one studio released two films that would haunt the century.
<!-- /hb-zoom -->
<!-- hb-story:start slug="bela-lugosi" name="Bela Lugosi" movie="Dracula (1931)" kind="famous" status="verified" -->
### Bela Lugosi

> **Who:** The Hungarian-born actor whose vampire became the face of the character forever.
> **When and where:** Hollywood, 1931.
> **Movie:** Dracula (1931), the film that made him a horror legend.

Bela Lugosi played Count Dracula with an accent and a stare that fixed the image of the vampire in the American mind. He was so tied to the role that he was eventually buried in the black cape.
<!-- hb-story:end slug="bela-lugosi" -->
<!-- hb-story:start slug="boris-karloff" name="Boris Karloff" movie="Frankenstein (1931)" kind="famous" status="verified" -->
### Boris Karloff

> **Who:** The actor whose flat-topped, bolt-necked creature became the most famous monster of all.
> **When and where:** Hollywood, 1931.
> **Movie:** Frankenstein (1931), released the same year as Dracula.

Boris Karloff, hidden under heavy makeup, played the stitched-together creature as a frightened, almost gentle giant. The look he wore is still what most people picture when they hear the word "monster."
<!-- hb-story:end slug="boris-karloff" -->
<!-- narrator pulls back out to the wider era again before the last fright of the period -->
<!-- hb-zoom level="span" label="panic on the airwaves" -->
Fear did not need a screen. On the night of October 30, 1938, a radio drama frightened part of its audience into thinking the country was truly under attack.
<!-- /hb-zoom -->
<!-- hb-story:start slug="orson-welles" name="Orson Welles" movie="" kind="famous" status="verified" -->
### Orson Welles

> **Who:** The young director whose radio play "The War of the Worlds" convinced some listeners a real invasion was underway.
> **When and where:** On the CBS radio network, October 30, 1938.

Orson Welles staged H. G. Wells's Martian invasion as a string of fake news bulletins, and some listeners who tuned in late took it for the real thing. The scale of the panic has grown in the retelling, but the broadcast proved how easily a voice in the dark could frighten a whole country.
<!-- hb-story:end slug="orson-welles" -->
<!-- closing era zoom: end the section back on the wide view -->
<!-- hb-zoom level="era" -->
The period closed with a mystery that would feed American imaginations for generations: in 1947, something crashed near Roswell, New Mexico, and the government's shifting story turned a desert wreck into the country's most famous tale of visitors from the sky.
<!-- /hb-zoom -->
<!-- hb-time:end id="1900-1950" -->

<!-- hb-time:start id="1950-2000" order="09" chapter="spooky-america" label="1950 to 2000" state="full" progress="written" -->
## 1950 to 2000
<!-- hb-zoom level="era" -->
In the second half of the century, American fear went looking for monsters in the real woods and packed the movie theaters to be scared on purpose.
<!-- /hb-zoom -->
<!-- hb-story:start slug="patterson-gimlin" name="Roger Patterson and Bob Gimlin" movie="" kind="ordinary" status="verified" -->
### Roger Patterson and Bob Gimlin

> **Who:** Two men who shot the most famous piece of Bigfoot film ever made.
> **When and where:** Bluff Creek, Northern California, 1967.

On an autumn day in 1967, Roger Patterson and Bob Gimlin filmed a large, dark, upright figure striding along a creek bed and glancing back over its shoulder. The short, shaky clip became the single most argued-over image in the whole legend of Bigfoot, and people are still fighting about it today.
<!-- hb-story:end slug="patterson-gimlin" -->
<!-- narrator pulls back to the wide view, then dives into the movie frights of the era -->
<!-- hb-zoom level="span" label="horror at the movies" -->
The bigger business, though, was on the screen, where scaring audiences became one of Hollywood's most reliable trades.
<!-- /hb-zoom -->
<!-- hb-story:start slug="william-peter-blatty" name="William Peter Blatty" movie="The Exorcist (1973)" kind="famous" status="verified" -->
### William Peter Blatty

> **Who:** The writer whose novel and screenplay about a possessed child terrified a nation.
> **When and where:** United States, novel 1971 and film 1973.
> **Movie:** The Exorcist (1973), which he adapted from his own novel.

William Peter Blatty based his story loosely on a real exorcism case he had read about as a college student. The film became one of the most frightening ever made, with reports of audiences fleeing theaters.
<!-- hb-story:end slug="william-peter-blatty" -->
<!-- hb-story:start slug="dan-aykroyd" name="Dan Aykroyd" movie="Ghostbusters (1984)" kind="famous" status="verified" -->
### Dan Aykroyd

> **Who:** The comic actor and lifelong paranormal enthusiast who co-wrote a movie about catching ghosts for a living.
> **When and where:** United States, 1984.
> **Movie:** Ghostbusters (1984), which he co-wrote and starred in.

Dan Aykroyd, who grew up in a family fascinated by the supernatural, turned the ghost story into a comedy about scientists with proton packs. The film made the spooky funny, and its theme song asked the question the whole decade seemed to enjoy answering.
<!-- hb-story:end slug="dan-aykroyd" -->
<!-- hb-story:start slug="blair-witch-filmmakers" name="Daniel Myrick and Eduardo Sanchez" movie="The Blair Witch Project (1999)" kind="famous" status="verified" -->
### Daniel Myrick and Eduardo Sanchez

> **Who:** The two filmmakers who ended the century with a low-budget horror movie that many viewers believed was real.
> **When and where:** United States, 1999.
> **Movie:** The Blair Witch Project (1999), shot to look like found footage.

Daniel Myrick and Eduardo Sanchez made their film look like real camcorder footage left behind by lost hikers, then used the young internet to spread the idea that it might be true. A generation walked out of theaters half-convinced it had watched something real.
<!-- hb-story:end slug="blair-witch-filmmakers" -->
<!-- hb-time:end id="1950-2000" -->

<!-- hb-time:start id="2000-today" order="10" chapter="spooky-america" label="2000 to Today" state="full" progress="written" -->
## 2000 to Today
<!-- hb-zoom level="era" -->
In our own time, American fear moved onto the internet, where anyone could invent a monster and share it with the world overnight. Ghost hunting also became a television staple, with crews stalking dark buildings on camera.
<!-- /hb-zoom -->
<!-- hb-story:start slug="eric-knudsen" name="Eric Knudsen" movie="" kind="ordinary" status="verified" -->
### Eric Knudsen

> **Who:** The man who created Slender Man, the first great monster born entirely on the internet.
> **When and where:** On an online forum, 2009.

In 2009, Eric Knudsen posted two edited photographs of a tall, faceless figure in a dark suit lurking behind children, and invented a monster called Slender Man. Strangers online kept adding stories and pictures until the character felt like an old legend, though it was only a few years old.
<!-- hb-story:end slug="eric-knudsen" -->
<!-- hb-time:end id="2000-today" -->


<!-- hb-chapter id="02" slug="sweet-tooth" title="Sweet Tooth" part="1" mode="prose" -->

# Chapter 2: Sweet Tooth

<!-- hb-note -->
**DEMO CHAPTER — throwaway test data, not part of the 35-chapter book.**
**Angle:** candy, treats, and dessert in America, and how a luxury became a daily habit.
**Shape:** one thin early cell (the sweet story mostly happens abroad at first), then it fills in.
This block is editor-only and is never shown to a reader; the final parser deletes every hb-note block.
<!-- /hb-note -->

<!-- hb-time:start id="before-1500" order="01" chapter="sweet-tooth" label="Before 1500" state="full" progress="written" -->
## Before 1500
<!-- hb-zoom level="era" -->
Long before sugar arrived, the peoples of this land already knew sweetness. It came from ripe berries and fruit, and, in the northern forests, from the trees themselves.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="maple sugaring" -->
Peoples of the northeastern woodlands tapped maple trees in late winter and boiled the running sap down into syrup and hard sugar. It was the first great sweet of this land, and the practice was old and skilled long before any European saw it.
<!-- /hb-zoom -->
<!-- hb-time:end id="before-1500" -->

<!-- hb-time:start id="1500s" order="02" chapter="sweet-tooth" label="The 1500s" state="thin" progress="written" -->
## The 1500s
<!-- hb-zoom level="era" -->
For this land the sweet century mostly happened elsewhere. After 1492, the great exchange of plants across the ocean set the whole future of American candy in motion, but almost none of it had reached these shores yet.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="sugar out, chocolate in" -->
Europeans carried sugarcane west and planted it in the Caribbean, while chocolate, a bitter drink prized by peoples of Mexico, traveled the other way to Spain. Both would one day flood into the future United States, but in the 1500s that was still far off.
<!-- /hb-zoom -->
<!-- hb-time:end id="1500s" -->

<!-- hb-time:start id="1600s" order="03" chapter="sweet-tooth" label="The 1600s" state="full" progress="written" -->
## The 1600s
<!-- hb-zoom level="era" -->
In the colonies, sweetness arrived by the barrel from the Caribbean sugar islands. Refined white sugar was costly, so most colonial baking leaned on something darker and cheaper.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="molasses, rum, and pies" -->
Molasses, the thick syrup left over from making sugar, sweetened colonial pies and puddings and was distilled into rum. That trade in sugar and molasses tied the colonies tightly, and uncomfortably, to the plantations and the slavery that produced it.
<!-- /hb-zoom -->
<!-- hb-time:end id="1600s" -->

<!-- hb-time:start id="1700-1750" order="04" chapter="sweet-tooth" label="1700 to 1750" state="full" progress="written" -->
## 1700 to 1750
<!-- hb-zoom level="era" -->
Refined sugar was still a luxury in the early 1700s, kept under lock like a treasure and shaved from a hard cone as needed. To serve something truly sweet was to show off a little.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="the first ice cream" -->
Among the wealthiest colonists a marvel began to appear at the table: ice cream, made by hand with ice hauled and stored at great trouble. A guest at the Maryland governor's house in 1744 wrote down his wonder at being served exactly that.
<!-- /hb-zoom -->
<!-- hb-time:end id="1700-1750" -->

<!-- hb-time:start id="1750-1800" order="05" chapter="sweet-tooth" label="1750 to 1800" state="full" progress="written" -->
## 1750 to 1800
<!-- hb-zoom level="era" -->
By the founding era, ice cream had become the favorite treat of the country's leaders, served at grand tables in Philadelphia and New York as a special delight.
<!-- /hb-zoom -->
<!-- hb-story:start slug="thomas-jefferson" name="Thomas Jefferson" movie="" kind="famous" status="verified" -->
### Thomas Jefferson

> **Who:** A founder and president who loved ice cream enough to write down how to make it.
> **When and where:** Virginia and the new nation, late 1700s.

Thomas Jefferson developed a taste for ice cream during his years in France and brought the fashion home. His handwritten recipe for vanilla ice cream still survives, one of the earliest American recipes for the treat we know today.
<!-- hb-story:end slug="thomas-jefferson" -->
<!-- hb-time:end id="1750-1800" -->

<!-- hb-time:start id="1800-1850" order="06" chapter="sweet-tooth" label="1800 to 1850" state="full" progress="written" -->
## 1800 to 1850
<!-- hb-zoom level="era" -->
As sugar grew cheaper, sweetness came down off the rich man's table and into the reach of ordinary children. Candy stopped being a luxury and started being a habit.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="penny candy and the soda fountain" -->
Small shops began selling brightly colored candies a single penny at a time, cheap enough for a child's pocket. In pharmacies, the soda fountain appeared, hissing out sweet flavored drinks over a marble counter.
<!-- /hb-zoom -->
<!-- hb-time:end id="1800-1850" -->

<!-- hb-time:start id="1850-1900" order="07" chapter="sweet-tooth" label="1850 to 1900" state="full" progress="written" -->
## 1850 to 1900
<!-- hb-zoom level="era" -->
In the last decades of the century, sweetness became a national industry. Familiar treats were born one after another: Coca-Cola arrived at an Atlanta soda fountain in 1886, Cracker Jack took its name in 1896, and Wrigley began selling chewing gum.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="chocolate for everyone" -->
The biggest change of all was chocolate. Once a costly drink for the rich, it was about to become a nickel bar in a child's hand, thanks to one determined candymaker.
<!-- /hb-zoom -->
<!-- hb-story:start slug="milton-hershey" name="Milton Hershey" movie="" kind="famous" status="verified" -->
### Milton Hershey

> **Who:** The candymaker who made milk chocolate cheap enough for ordinary Americans.
> **When and where:** Pennsylvania, late 1800s into the early 1900s.

Milton Hershey made his first fortune selling caramels, then bet it all on mass-producing milk chocolate. His methods drove the price down until a chocolate bar became something almost anyone could afford, and he built a whole town around his factory.
<!-- hb-story:end slug="milton-hershey" -->
<!-- hb-time:end id="1850-1900" -->

<!-- hb-time:start id="1900-1950" order="08" chapter="sweet-tooth" label="1900 to 1950" state="full" progress="written" -->
## 1900 to 1950
<!-- hb-zoom level="era" -->
The first half of the new century was a golden age of American treats. The ice cream cone was popularized at the 1904 World's Fair in St. Louis, the Oreo appeared in 1912, and candy bars poured off the assembly lines by the dozen.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="a happy accident" -->
The era's most beloved dessert, though, was born by mistake in a New England inn kitchen.
<!-- /hb-zoom -->
<!-- hb-story:start slug="ruth-wakefield" name="Ruth Wakefield" movie="" kind="ordinary" status="verified" -->
### Ruth Wakefield

> **Who:** The innkeeper and cook who invented the chocolate chip cookie.
> **When and where:** The Toll House Inn, Whitman, Massachusetts, in the 1930s.

Ruth Wakefield ran a popular roadside inn and cut a chocolate bar into small chunks to fold into her cookie dough, expecting it to melt and blend in. Instead the chunks held their shape, and the chocolate chip cookie was born, soon famous across the country as the Toll House cookie.
<!-- hb-story:end slug="ruth-wakefield" -->
<!-- hb-time:end id="1900-1950" -->

<!-- hb-time:start id="1950-2000" order="09" chapter="sweet-tooth" label="1950 to 2000" state="full" progress="written" -->
## 1950 to 2000
<!-- hb-zoom level="era" -->
By mid-century candy was everywhere: a whole aisle of the grocery store, a fixture of movie theaters, and the treasure of every trick-or-treat bag. Sweetness had become a full part of American childhood.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="a chocolate factory on screen" -->
Then Hollywood turned the candy dream into a movie that fixed it in the imagination of every child who saw it.
<!-- /hb-zoom -->
<!-- hb-story:start slug="roald-dahl" name="Roald Dahl" movie="Willy Wonka & the Chocolate Factory (1971)" kind="famous" status="verified" -->
### Roald Dahl

> **Who:** The author whose book about a magical chocolate factory became a beloved film.
> **When and where:** Book published 1964; film released 1971.
> **Movie:** Willy Wonka & the Chocolate Factory (1971), starring Gene Wilder.

Roald Dahl wrote "Charlie and the Chocolate Factory," a tale of golden tickets and a candymaker's secret rooms. The 1971 film turned it into pure sweet spectacle, from a chocolate river to a room where everything was good enough to eat.
<!-- hb-story:end slug="roald-dahl" -->
<!-- hb-time:end id="1950-2000" -->

<!-- hb-time:start id="2000-today" order="10" chapter="sweet-tooth" label="2000 to Today" state="full" progress="written" -->
## 2000 to Today
<!-- hb-zoom level="era" -->
In our own time, dessert became a kind of show. The plain treats of childhood were reinvented as small luxuries, photographed and lined up in glass cases.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="the cupcake craze" -->
The clearest sign was the cupcake craze of the 2000s, when boutique bakeries built long lines and whole shops out of a single frosted cake. A humble birthday-party treat became, for a while, the height of fashion.
<!-- /hb-zoom -->
<!-- hb-time:end id="2000-today" -->


<!-- hb-chapter id="03" slug="thinking-machines" title="Thinking Machines" part="1" mode="prose" -->

# Chapter 3: Thinking Machines

<!-- hb-note -->
**DEMO CHAPTER — throwaway test data, not part of the 35-chapter book.**
**Angle:** counting and thinking machines in America, from fingers to artificial intelligence.
**Why it shows the empty and thin cells:** for the first centuries these machines simply did not exist here, or existed only abroad. This lens is the demo's test of `state="empty"` and `state="thin"`.
This block is editor-only and is never shown to a reader; the final parser deletes every hb-note block.
<!-- /hb-note -->

<!-- empty era: the subject did not exist here yet. state=empty, one era zoom, no story. -->
<!-- hb-time:start id="before-1500" order="01" chapter="thinking-machines" label="Before 1500" state="empty" progress="written" -->
## Before 1500
<!-- hb-zoom level="era" -->
There were no thinking machines in this land, and none anywhere that we would call a computer. People counted the way people always had: on their fingers, with pebbles and marked tally sticks, and, in some places, with knotted cords. There is nothing here to tell of machines, because the machines had not been imagined.
<!-- /hb-zoom -->
<!-- hb-time:end id="before-1500" -->

<!-- second empty era: still nothing here; what exists is all abroad. state=empty. -->
<!-- hb-time:start id="1500s" order="02" chapter="thinking-machines" label="The 1500s" state="empty" progress="written" -->
## The 1500s
<!-- hb-zoom level="era" -->
Still nothing here. Across the ocean, merchants reckoned on the bead-and-wire abacus and craftsmen built intricate mechanical clocks, but none of that had reached this land. From the angle of the thinking machine, these shores were silent.
<!-- /hb-zoom -->
<!-- hb-time:end id="1500s" -->

<!-- thin era: the story exists, but only abroad. state=thin. -->
<!-- hb-time:start id="1600s" order="03" chapter="thinking-machines" label="The 1600s" state="thin" progress="written" -->
## The 1600s
<!-- hb-zoom level="era" -->
The first true calculating machine appeared in this century, but far away. In the colonies, every sum was still worked out by hand, with pen, paper, and patience.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="Pascal's calculator, abroad" -->
In France in 1642, a young Blaise Pascal built a brass machine of turning wheels that could add and subtract. It was a wonder of Europe, and an ocean away from the American colonists who would not see such a thing for generations.
<!-- /hb-zoom -->
<!-- hb-time:end id="1600s" -->

<!-- thin era: again the marvels are all overseas. state=thin. -->
<!-- hb-time:start id="1700-1750" order="04" chapter="thinking-machines" label="1700 to 1750" state="thin" progress="written" -->
## 1700 to 1750
<!-- hb-zoom level="era" -->
In Europe, clockmakers were building astonishing mechanical figures that could write, draw, or play music, and grand clocks that modeled the heavens. In the American colonies there was little of this; the work of calculation stayed in the head and on the page.
<!-- /hb-zoom -->
<!-- hb-time:end id="1700-1750" -->

<!-- full era at last: a real American computer, and he was a person. state=full. -->
<!-- hb-time:start id="1750-1800" order="05" chapter="thinking-machines" label="1750 to 1800" state="full" progress="written" -->
## 1750 to 1800
<!-- hb-zoom level="era" -->
As the country was founded, the hardest "computing" it needed was still done by human minds. To predict the motions of the sun, moon, and stars for a printed almanac took long chains of arithmetic, all by hand.
<!-- /hb-zoom -->
<!-- hb-story:start slug="benjamin-banneker" name="Benjamin Banneker" movie="" kind="famous" status="verified" -->
### Benjamin Banneker

> **Who:** A free Black man and self-taught astronomer who calculated his own almanacs by hand.
> **When and where:** Maryland, in the 1790s.

Benjamin Banneker taught himself mathematics and astronomy, once building a working striking clock out of carved wood. In the 1790s he worked out the long calculations for a series of published almanacs entirely by hand, a human computer at a time when the machine did not yet exist here.
<!-- hb-story:end slug="benjamin-banneker" -->
<!-- hb-time:end id="1750-1800" -->

<!-- thin era: the great engines are dreamed up in England, not here. state=thin. -->
<!-- hb-time:start id="1800-1850" order="06" chapter="thinking-machines" label="1800 to 1850" state="thin" progress="written" -->
## 1800 to 1850
<!-- hb-zoom level="era" -->
The idea of a machine that could compute anything was born in this era, but again across the sea.
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="Babbage's engines, in England" -->
In England, Charles Babbage designed vast geared "engines" meant to calculate and even to follow programmed instructions. They were mostly never built in his lifetime, and America, still doing its figures by hand, took little notice.
<!-- /hb-zoom -->
<!-- hb-time:end id="1800-1850" -->

<!-- full era: the first American computing machine, and the person behind it. state=full. -->
<!-- hb-time:start id="1850-1900" order="07" chapter="thinking-machines" label="1850 to 1900" state="full" progress="written" -->
## 1850 to 1900
<!-- hb-zoom level="era" -->
Near the century's end, the United States built its first great counting machine to solve a very American problem: a national census that had grown too large to add up by hand in time.
<!-- /hb-zoom -->
<!-- hb-story:start slug="herman-hollerith" name="Herman Hollerith" movie="" kind="famous" status="verified" -->
### Herman Hollerith

> **Who:** The inventor whose punch-card machine counted the 1890 census.
> **When and where:** Washington, D.C., 1890.

The 1880 census had taken years to tally by hand. Herman Hollerith invented a machine that read holes punched in cards, and it counted the 1890 census in a fraction of the time. The company he founded to sell it would, decades later, grow into IBM.
<!-- hb-story:end slug="herman-hollerith" -->
<!-- hb-time:end id="1850-1900" -->

<!-- full era with TWO stories and the narrator zooming back out between them. state=full. -->
<!-- hb-time:start id="1900-1950" order="08" chapter="thinking-machines" label="1900 to 1950" state="full" progress="written" -->
## 1900 to 1950
<!-- hb-zoom level="era" -->
In the 1940s the electronic computer was born, in secret and in a hurry, driven by the needs of the Second World War. In 1946 the United States unveiled ENIAC, a room-sized machine of thousands of glowing tubes.
<!-- /hb-zoom -->
<!-- hb-story:start slug="eniac-programmers" name="The ENIAC Programmers" movie="" kind="ordinary" status="verified" -->
### The ENIAC Programmers

> **Who:** Six women who programmed the first great American electronic computer.
> **When and where:** Philadelphia, 1945 and 1946.

While men built ENIAC's hardware, six women were assigned to make it actually work, programming it by physically setting switches and plugging in cables. They figured out how to run its problems with almost no manual to guide them, and for years their names were left out of the story.
<!-- hb-story:end slug="eniac-programmers" -->
<!-- new era-level zoom after a story = narrator pulling back to the wide view before the next person -->
<!-- hb-zoom level="span" label="a moth in the machine" -->
Elsewhere, another pioneer was giving the young field one of its favorite words, thanks to a real insect.
<!-- /hb-zoom -->
<!-- hb-story:start slug="grace-hopper" name="Grace Hopper" movie="" kind="famous" status="verified" -->
### Grace Hopper

> **Who:** A Navy officer and computer scientist who helped make computers easier to instruct.
> **When and where:** Harvard, 1947, and the decades after.

In 1947, a real moth was found trapped in a Harvard computer's relays, and the team taped it into their logbook as the first actual "bug." Grace Hopper loved to tell the story, and she went on to help invent ways of programming with words instead of raw numbers, opening computers to far more people.
<!-- hb-story:end slug="grace-hopper" -->
<!-- hb-time:end id="1900-1950" -->

<!-- full era: the machine comes home and starts to beat us at our own games. state=full. -->
<!-- hb-time:start id="1950-2000" order="09" chapter="thinking-machines" label="1950 to 2000" state="full" progress="written" -->
## 1950 to 2000
<!-- hb-zoom level="era" -->
In the second half of the century the computer shrank from a room to a desk and arrived in ordinary homes as the personal computer. As it did, Americans grew both amazed and uneasy, and their movies dreamed of machines that turned on us, from the calm, murderous HAL of 2001: A Space Odyssey (1968) to the killer robot of The Terminator (1984).
<!-- /hb-zoom -->
<!-- hb-zoom level="span" label="checkmate" -->
Then, at the very end of the century, a machine beat the finest human mind at a game long treated as pure human genius.
<!-- /hb-zoom -->
<!-- hb-story:start slug="garry-kasparov" name="Garry Kasparov and Deep Blue" movie="" kind="famous" status="verified" -->
### Garry Kasparov and Deep Blue

> **Who:** The reigning world chess champion, defeated by an IBM computer.
> **When and where:** New York City, 1997.

Garry Kasparov was the greatest chess player in the world when he sat down against IBM's Deep Blue in 1997. The machine won the match, the first time a computer had beaten a reigning world champion under tournament rules, and many felt a line had quietly been crossed.
<!-- hb-story:end slug="garry-kasparov" -->
<!-- hb-time:end id="1950-2000" -->

<!-- full era: the machine in every pocket, and now it talks back. state=full. -->
<!-- hb-time:start id="2000-today" order="10" chapter="thinking-machines" label="2000 to Today" state="full" progress="written" -->
## 2000 to Today
<!-- hb-zoom level="era" -->
In our own time the thinking machine went from the desk into every pocket. The iPhone arrived in 2007, and soon a computer more powerful than ENIAC rode along on the daily bus. Then the machines began to answer back: a program called ChatGPT reached the public in 2022 and set off a boom in artificial intelligence.
<!-- /hb-zoom -->
<!-- hb-story:start slug="ken-jennings" name="Ken Jennings" movie="" kind="famous" status="verified" -->
### Ken Jennings

> **Who:** The greatest human champion of the quiz show Jeopardy, beaten by a computer.
> **When and where:** On national television, 2011.

Ken Jennings had won more games of Jeopardy than anyone alive when he faced IBM's Watson in 2011. The computer won, and Jennings took it in good humor, joking as he wrote, "I, for one, welcome our new computer overlords." It was a friendly echo of the old fear that the thinking machine might one day outthink us all.
<!-- hb-story:end slug="ken-jennings" -->
<!-- hb-time:end id="2000-today" -->
