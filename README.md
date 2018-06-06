Set of tools to scan Diablo 2 files

## Recipe

A scanner for recipes and items, pass it the root directory of the exported txt files from the bin files (you can have D2 export them itself), built for D2 1.10 but should work on any(?).

Example usage:

```zsh
─➤  python3 recipe.py /mnt/storage0/Games/Blizzard/Diablo2/Diablo\ II/MODS/zyel/data/global/excel
-- Importing recipes
-- Importing recipes complete (1.697s)
-- Importing items
-- Importing items complete (0.217s)
-- Processing cases...
-- Processing cases complete (0.094s)
-- Processing names
-- Processing names complete (0.007s)

Enter command ('help' for help, 'quit' to quit):
> ?

Known commands:
?: Show this help
help: Show this help
id: Show Item Details by code
in: Search item names, the item code is listed first on each line
quit: Exit the program
ri: Search Recipes by item code
rin: Search Recipes by item names

Enter command ('help' for help, 'quit' to quit):                                                                           [84/1817]
> rin finder

Item ChoM3-Finder (cj4) type: chm3
Item ChoM2-Finder (ci4) type: chm2
Item ChoM-Finder (ch4) type: chm1

Scanning: 00% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100% 

collector chom1 : "collector (fa0)" <- "collector (fa0)" + chm1
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=2"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=3"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=4"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=5"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=6"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=7"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=8"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=9"
collector chom1 : "collector (fa0)" <- "collector (fa0)" + "chm1,qty=10"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + chm2
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=2"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=3"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=4"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=5"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=6"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=7"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=8"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=9"
collector chom2 : "collector (fa0)" <- "collector (fa0)" + "chm2,qty=10"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=2"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=3"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=4"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=5"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=6"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=7"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=8"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=9"
collector chom3 : "collector (fa0)" <- "collector (fa0)" + "chm3,qty=10"
extractor chom : useitem + "extractor (fa1)" + chomhealer <- chm1 + "extractor (fa1)"
extractor chom : useitem + "extractor (fa1)" + chom2healer <- chm2 + "extractor (fa1)"
extractor chom : useitem + "extractor (fa1)" + chom3healer <- chm3 + "extractor (fa1)"
upgrader chom : chom2healer + "upgrader (fa2)" <- chm1 + "upgrader (fa2)"
upgrader chom : chom3healer + "upgrader (fa2)" <- chm2 + "upgrader (fa2)"
dbox : "yuck - bad message (u98)" <- "mephisto key (luv)" + "chom-finder (ch4)"
dbox : "demon box #923 (ca4)" <- "mephisto key (luv)" + "chom2-finder (ci4)"
dbox : "demon box #933 (cb4)" <- "mephisto key (luv)" + "chom3-finder (cj4)"
dbox : "chom-finder (ch4)" <- "mephisto key (luv)" + "demon box #1073 (cp4)"
poster major : "ghost hat (ces)" <- "chom-destroyer (ch3)" + "chom-finder (ch4)" + "chom-flamer (ch5)" + "chom-healer (ch6)"
chom : chom2healer <- "chm1,qty=3" + "gem4,qty=3" + "char,crf" + "jewel (jew)",crf + "cbs2,qty=3"
chom : chom3healer <- "chm2,qty=3" + "gem6,qty=3" + "char,uni" + "jewel (jew)",uni + "cbs3,qty=3"
chom : chombuzzer <- chm1 + "chipped topaz (gcy)",qty=2
chom : chomcrusader <- chm1 + "chipped diamond (gcw)",qty=3
chom : chomdefender <- chm1 + "chipped diamond (gcw)",qty=2
chom : chomdestroyer <- chm1 + "chipped amethyst (gcv)",qty=3
chom : chomfinder <- chm1 + "chipped diamond (gcw)" + "chipped topaz (gcy)"
chom : chomflamer <- chm1 + "chipped ruby (gcr)",qty=2
chom : chomhealer <- chm1 + "chipped emerald (gcg)"
chom : chomicer <- chm1 + "chipped saphire (gcb)",qty=2
chom : chommarauder <- chm1 + "chipped skull (skc)" + "chipped emerald (gcg)"
chom : chommaster <- chm1 + "chipped diamond (gcw)" + "chipped amethyst (gcv)"
chom : chompsycho <- chm1 + "chipped topaz (gcy)" + "chipped diamond (gcw)" + "chipped emerald (gcg)" + "chipped saphire (gcb)" + "c
hipped ruby (gcr)"
chom : chomshield <- chm1 + "chipped diamond (gcw)"
chom : chomskull <- chm1 + "chipped skull (skc)"
chom : chomslayer <- chm1 + "chipped amethyst (gcv)" + "chipped ruby (gcr)"
chom : chomslogger <- chm1 + "chipped saphire (gcb)"
chom : chomspeed <- chm1 + "chipped topaz (gcy)",qty=3
chom : chomsponge <- chm1 + "chipped ruby (gcr)" + "chipped saphire (gcb)" + "chipped topaz (gcy)"
chom : chomsummoner <- chm1 + "chipped skull (skc)" + "chipped diamond (gcw)"
chom : chomvenom <- chm1 + "chipped emerald (gcg)",qty=2
chom : chom2buzzer <- chm2 + "topaz (gsy)",qty=2
chom : chom2crusader <- chm2 + "diamond (gsw)",qty=3
chom : chom2defender <- chm2 + "diamond (gsw)",qty=2
chom : chom2destroyer <- chm2 + "amethyst (gsv)",qty=3
chom : chom2finder <- chm2 + "diamond (gsw)" + "topaz (gsy)"
chom : chom2flamer <- chm2 + "ruby (gsr)",qty=2
chom : chom2healer <- chm2 + "emerald (gsg)"
chom : chom2icer <- chm2 + "saphire (gsb)",qty=2
chom : chom2marauder <- chm2 + "skull (sku)" + "emerald (gsg)"
chom : chom2master <- chm2 + "diamond (gsw)" + "amethyst (gsv)"
chom : chom2psycho <- chm2 + "topaz (gsy)" + "diamond (gsw)" + "emerald (gsg)" + "saphire (gsb)" + "ruby (gsr)"
chom : chom2shield <- chm2 + "diamond (gsw)"
chom : chom2skull <- chm2 + "skull (sku)"
chom : chom2slayer <- chm2 + "amethyst (gsv)" + "ruby (gsr)"
chom : chom2slogger <- chm2 + "saphire (gsb)"
chom : chom2slogger <- chm2 + "saphire (gsb)"
chom : chom2speed <- chm2 + "topaz (gsy)",qty=3
chom : chom2sponge <- chm2 + "ruby (gsr)" + "saphire (gsb)" + "topaz (gsy)"
chom : chom2summoner <- chm2 + "skull (sku)" + "diamond (gsw)"
chom : chom2venom <- chm2 + "emerald (gsg)",qty=2
chom : chom3buzzer <- chm3 + "perfect topaz (gpy)",qty=2
chom : chom3crusader <- chm3 + "perfect diamond (gpw)",qty=3
chom : chom3defender <- chm3 + "perfect diamond (gpw)",qty=2
chom : chom3destroyer <- chm3 + "perfect amethyst (gpv)",qty=3
chom : chom3finder <- chm3 + "perfect diamond (gpw)" + "perfect topaz (gpy)"
chom : chom3flamer <- chm3 + "perfect ruby (gpr)",qty=2
chom : chom3healer <- chm3 + "perfect emerald (gpg)"
chom : chom3icer <- chm3 + "perfect saphire (gpb)",qty=2
chom : chom3marauder <- chm3 + "perfect skull (skz)" + "perfect emerald (gpg)"
chom : chom3master <- chm3 + "perfect diamond (gpw)" + "perfect amethyst (gpv)"
chom : chom3psycho <- chm3 + "perfect topaz (gpy)" + "perfect diamond (gpw)" + "perfect emerald (gpg)" + "perfect saphire (gpb)" + "
perfect ruby (gpr)"
chom : chom3shield <- chm3 + "perfect diamond (gpw)"
chom : chom3skull <- chm3 + "perfect skull (skz)"
chom : chom3slayer <- chm3 + "perfect amethyst (gpv)" + "perfect ruby (gpr)"
chom : chom3slogger <- chm3 + "perfect saphire (gpb)"
chom : chom3speed <- chm3 + "perfect topaz (gpy)",qty=3
chom : chom3sponge <- chm3 + "perfect ruby (gpr)" + "perfect saphire (gpb)" + "perfect topaz (gpy)"
chom : chom3summoner <- chm3 + "perfect skull (skz)" + "perfect diamond (gpw)"
chom : chom3venom <- chm3 + "perfect emerald (gpg)",qty=2

Enter command ('help' for help, 'quit' to quit):
> in finder

ch4 - ChoM-Finder -  - 
ci4 - ChoM2-Finder -  - 
cj4 - ChoM3-Finder -  - 

Enter command ('help' for help, 'quit' to quit):
> id ch4

namestr: Ch4
level: 99
HellUpgrade: xxx
component: 16
ElzixMagicLvl: 255
usesound: item_charm
alternategfx: rld
LarzukMagicLvl: 255
name: ChoM-Finder
rarity: 231
CainMagicLvl: 255
dropsfxframe: 12
gamble cost: 48000
NightmareUpgrade: xxx
LysanderMagicLvl: 255
BetterGem: non
cost: 200000
levelreq: 10
MalahMagicLvl: 255
invwidth: 2
HalbuMagicLvl: 255
AlkorMagicLvl: 255
invfile: chmfinder
OrmusMagicLvl: 255
JamellaMagicLvl: 255
transtbl: 5
spellicon: -1
AshearaMagicLvl: 255
flippyfile: flpchm2
DrehyaMagicLvl: 255
GheedMagicLvl: 255
dropsound: item_charm
version: 100
invheight: 2
TMogType: xxx
CharsiMagicLvl: 255
HraltiMagicLvl: 255
AkaraMagicLvl: 255
FaraMagicLvl: 255
type: chm1
nodurability: 1
code: ch4
DrognanMagicLvl: 255

Enter command ('help' for help, 'quit' to quit):
> ri ch4

Scanning: 00% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100% 

dbox : "yuck - bad message (u98)" <- "mephisto key (luv)" + "chom-finder (ch4)"
dbox : "chom-finder (ch4)" <- "mephisto key (luv)" + "demon box #1073 (cp4)"
poster major : "ghost hat (ces)" <- "chom-destroyer (ch3)" + "chom-finder (ch4)" + "chom-flamer (ch5)" + "chom-healer (ch6)"

Enter command ('help' for help, 'quit' to quit):
> quit
```

