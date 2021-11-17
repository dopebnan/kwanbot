# Changelog 

## Time Spent Coding: 50.5 hours



# Cleanup Update
<sub>Unreleased</sub>

## Code
* [x] Removed unused functions (commit#285486f)
* [x] Fixed **bot2-4_play-2** (commit#285486f)
* [ ] make code look nice and clean and neat and good and shit


## DevTools 1.1.1

## Shortcut
* [x] Fixed formatting error for **nowPalying** (commit#285486f)
* [ ] Refactoring everything. This is a mess. This isn't okay. Why did i do it like that. Stop it.
* [ ] Make DevTool errors more verbose

## Configs
* [x] Added **r!pain** values (commit#285486f)

## UX
* [x] Added **r!pain**, pics that invoked pain while coding the bot (commit#285486f)  <sub>idea by pigon</sub>

## UX (DevTools)
* [ ] Added **r!painDev Cooldown int**, change **r!pain** cooldown 

## Misc
* [x] Reformatted the changelog (commit#9ea5819)

## TSC: 2.5h


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

## UX
* [x] Added **r!bugtracker**, you can check out the bugs there now (commit#ef958c2)
* [x] Added **r!cum**, queues the cum trilogy (commit#cedcf86)
* [x] Added **r!leave**, makes bot leave vc	(commit#cedcf86)
* [x] Added **r!pause**, pauses/unpauses current song (commit#cedcf86)
* [x] Added **r!play %songname%**, plays *songname* (commit#cedcf86)
* [x] Added **r!playlocal %songname%**, plays a locally downloaded song (commit#cedcf86)
* [x] Added **r!pop**, makes bot pop into vc (commit#cedcf86)
* [x] Added **r!skip**, skips current song (commit#cedcf86)
* [x] Added **r!songlist**, lists all locally downloaded songs (commit#cedcf86)

## UX (DevTools)
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

## UX
* [x] Removed **sorry bot** (commit#55a03cc)

## UX (DevTools)
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

## UX
* [x] Added **r!changelog**, you can now see the changelog, *you're looking at it rn!*
* [x] **r!check** now displays time passed since last update
* [x] Added **r!ping**, see the latency of the bot
* [x] Removed **giv pic**, because **r!pic** was enough
* [x] **glori** Replaced that If chunk with one if for IDs
* [x] Started removing **sorry bot**

## UX (DevTools)
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
