# Changelog 

!! You should use a proper markdown viewer !!

## Time Spent Coding: 56 hours

# v2.3 - LINUX UPDATE!!!
<sub>Jan. 21, 2022</sub>

## Code
* [x] Made code more pythonic  (commit#91edc69)
  * [x] reformatted/organized code  (commit#91edc69)
* [x] Improved Cogs.Gruvi  (commit#284f391)
* [x] Moved bugs to GitHub Issue tracker  (commit#eab8469)
* [x] Added 24/7 hosting, thanks to moving to a Raspberry Pi!  (commit#ccb4df70)

## Shortcuts
* [x] split `shortcuts.py` into `shortcuts.py` and `embeds.py`  (commit#91edc692)
* [x] removed classes from `shortcuts.py`  (commit#91edc692)

## UI
* [x] Added **r!playfile**, you can send the bot files to play now
* [x] `r!report` now links you to the bot's GitHub page  (commit#eab8469)
* [x] Made it so that running the bot without any pictures doesn't crash it
* [x] Removed `r!bugtracker`, it's now on GitHub  (commit#eab8469)

## BETA
* [x] **r!remove**, it's still under heavy work, but it works... kinda..? maybe not that much  (commit#58585d45)

## TSC: 12h 

# v2.2 - CLEANUP UPDATE!!!
<sub>Nov. 22, 2021</sub>

## Code
* [x] When **settings.json** is missing, bot makes a new one, instead of force-quitting (commit#026817f)
* [x] Moved all logging and message sends at the end of the error-handling function, no more code repetition (commit#a1c2e39)
* [x] Removed all variable type checks in the error-handling function, for optimization (commit#a1c2e39)
* [x] Removed most command checks in the error-handling function, for optimization (commit#a1c2e39)
* [x] Removed unused functions (commit#285486f)
* [x] Removed config file checks from cogs (commit#026817f)
* [x] Fixed **bot2-4_play-2** (commit#285486f)

## DevTools 1.1.1
* [x] Tidied up embeds (commit#a1c2e39)
* [x] Removed unused TRY functions (commit#a1c2e39)
* [x] Removed variable type checks (commit#a1c2e39)
* [x] Removed unused functions (commit#a1c2e39)
* [x] Removed config file checks (commit#026817f)

## Shortcut
* [x] Added a **logging()** function, where it doesn't log the full message *(useful for logging messages)* (commit#a1c2e39)
* [x] Refactored and reorganized embeds, because they weren't (commit#a1c2e39)
* [x] Removed **self** variable from functions that weren't using it (commit#a1c2e39)
* [x] Removed unused code (commit#a1c2e39)
* [x] Fixed formatting error for **nowPlaying** (commit#285486f)
* [x] Fixed typos (commit#a1c2e39)

## Configs
* [x] Added **r!pain** values (commit#285486f)
* [x] Added **version.json**, and moved the version stuff from **config.json** to **version.json** (commit#026817f)

## UI
* [x] Added **r!pain**, pics that invoked pain while coding the bot (commit#285486f)  <sub>idea by pigon</sub>

## UI (DevTools)
* [x] Added **r!painDev Cooldown int**, change **r!pain** cooldown (commit#59011a4)
* [x] Added **r!painDev Return bool**, if **r!pain** should return the cooldown after pics (commit#59011a4)
* [x] Changed every command that takes a boolean. They now take integers as booleans (0 -> False, 1 -> True). Was needed for optimization. (commit#a1c2e39)
    *(Ex. r!autoDev Switch True -> r!autoDev Switch 1)*
* [x] Made **r!log %msg%** only log messages (commit#026817f)
* [x] Started logging error messages too (commit#026817f)

## Misc
* [x] Reformatted the changelog (commit#9ea5819)

## TSC: 6h


# v2.1 - GRUVI'S SPIRIT UPDATE!! I.
<sub>Oct. 21, 2021</sub>

## Code
* [x] Changed the way logging works when an error happens (commit#b2dd861)
* [x] Made UnknownError actually parse the error into the logs (commit#c253fcb)
* [x] Moved the help embeds to **help.py** (commit#c253fcb)
* [x] Tidied up embeds (commit#c253fcb)
* [x] Removed trailing whitespace and too many newlines (commit#c253fcb)
* [x] Removed unused functions (commit#c253fcb)
* [x] Clarified bugs in **bugtracker.md** (commit#c253fcb)

## DevTools 1.1
* [x] Tidied up embeds (commit#b2dd861)
* [x] Moved the help embeds to **help.py** (commit#c253fcb)

## Shortcut
* [x] Added a string parser for local songs (commit#b2dd861)
* [x] Added a queue formatter (commit#b2dd861)
* [x] Added more embeds (commit#b2dd861)

## Configs
* [x] Reformatted config.json (commit#b2dd861)

## UI
* [x] Added **r!bugtracker**, you can check out the bugs there now (commit#ef958c2)
* [x] Added **r!cum**, queues the cum trilogy (commit#cedcf86)
* [x] Added **r!leave**, makes bot leave vc	(commit#cedcf86)
* [x] Added **r!pause**, pauses/unpauses current song (commit#cedcf86)
* [x] Added **r!play %songname%**, plays *songname* (commit#cedcf86)
* [x] Added **r!playlocal %songname%**, plays a locally downloaded song (commit#cedcf86)
* [x] Added **r!pop**, makes bot pop into vc (commit#cedcf86)
* [x] Added **r!skip**, skips current song (commit#cedcf86)
* [x] Added **r!songlist**, lists all locally downloaded songs (commit#cedcf86)

## UI (DevTools)
* [x] Added **r!newlog**, creates new log.txt. Does NOT delete old log. *Old logs can only be accessed locally.* (commit#b2dd861)
* [x] Made **r!log** able to log comments too (commit#c253fcb)

## TSC: 20h


# v2.0.1 - Open Source Update
<sub>Sep. 13, 2021</sub>

## Code
* [x] Moved all lists to the top of **bot.py**(commit#55a03cc)
* [x] Refactored **temp.py** into discord.ext (commit#55a03cc)
  * [x] Added changing statuses
  * [x] Added embeds
* [x] Fixed bug where bot wouldn't respond to requests (commit#55a03cc)
* [x] Fixed **bot2-1_uwu-1**. where bot didn't work in the %uwuChannel% (commit#55a03cc)

## Configs
* [x] Added **"uwuChannel"**, and **"uwuIDs"** variables to **config.json** (commit#55a03cc)

## UI
* [x] Removed **sorry bot** (commit#55a03cc)

## UI (DevTools)
* [x] Added **r!sourcecode**, you can check the source code of kwanbot. *You don't need DevTool perms to use this command.* (commit#55a03cc)

## TSC: 2h


# v2.0 - discord.ext UPDATE!!
<sub>Sep. 18, 2021</sub>

Everything here happened in commit#2471c74

## Code 

### bot.py
* [x] Started using functions instead of global variables, like a normal person (what the fuck was I doing back then)
* [x] Changed variable names, to make them make sense
* [x] Moved hardcoded IDs into **config.json**
* [x] Started using a **discord.Bot()** instead of a **discord.Client()**
* [x] Added changing status thingy
* [x] Started using cogs
* [x] Started using embeds
* [x] Moved DevTools into **Cogs.DevTools**
* [x] Moved commands into **Cogs.General**
* [x] Added error handling for commands
* [x] Fixed bug where bot thought *just* was *jus*

### Cogs.General
* [x] Started using embeds
* [x] Added Asynchronous cooldown
* [x] Started using normal variable names
* [x] **r!pic**
  * [x] Replaced IFs and TRYs with one IF
  * [x] Added messages next to images
* [x] **r!autopic**
  * [x] Reduced the amount of nested IFs
  * [x] Used Async sleep instead of Sync sleep
* [x] **r!uwu**
  * [x] Replaced image messages with variation of uwu
  * [x] Reduced nested IFs, removed nested TRYs

## DevTools 1.0
* [x] Started using embeds
* [x] Hardcoded **config.json**'s factory settings
* [x] Hardcoded debug template for **config.json**
* [x] **r!filecheck**
  * [x] Reformatted it
  * [x] Made it display, in addition, the settings.json tag, the DevTools version, Bot ID, API version, and, the current Python version that the bot is running on
* [x] Added errror handling to **r!reset**
* [x] Removed most nested IFs (what the fuck was wrong with me)

## Shortcut
*Self made module/framework that has many shortcuts for discord bots*
* [x] **fileType()**, tell you the type of variable
* [x] **logging()**, self-made logging function. logs to file, not terminal
* [x] **Embeds**, class that has many embed templates

## Configs
* [x] Changed **data.py** into **config.json** and **settings.json**
* [x] Made backups of these in **assets/backups**

## UI
* [x] Added **r!changelog**, you can now see the changelog, *you're looking at it rn!*
* [x] **r!check** now displays time passed since last update
* [x] Added **r!ping**, see the latency of the bot
* [x] Removed **giv pic**, because **r!pic** was enough
* [x] **glori** Replaced that If chunk with one if for IDs
* [x] Started removing **sorry bot**

## UI (DevTools)
* [x] Added **r!debug**, changes **config.json** into debug mode
* [x] Added **r!log**, gives you the log file in DMs
* [x] Added **r!reload**, reloads the config files
* [x] Changed **d!help** to **r!devtools**
* [x] Changed **d!check** to **r!filecheck**
* [x] Changed **d!default** to **r!reset**
* [x] Changed syntax of most of the commands
  * **d!pic int** -> **r!picDev Cooldown int**
  * **d!pic return bool** -> **r!picDev Return bool**
  * **d!autopic bool** -> **r!autoDev Switch bool**
  * **d!uwu bool** -> **r!uwuDev Switch bool**
  * **d!uwu time int** -> **r!uwuDev Cooldown int**
  * **d!uwu return bool** -> **r!uwuDev Return bool**
* [x] Removed **d!restart**, **r!reload** is more optimal
* [x] Removed **d!save**, bot auto-save, you don't need to manually save anymore

## Misc
* [x] Reorganized image names

## TSC: 26h
