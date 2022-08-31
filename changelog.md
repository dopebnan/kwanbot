# Changelog

## v3.1 - dpy v2.0 Update !!
<sub>Aug 31, 2022</sub>
### UX
#### Added
* **General**:
  * **r!add_to_cart**: You can add random stuff to your cart! (thanks kwan)

#### Changed
* **Devs**:
  * **r!update**: Bot restarts after update to apply everything

#### Fixed
* **General**:
  * **r!autopic**: Now it works

### Code
#### Changed
* Rewrote main parts in dpy v2.0

## v3.0.1 - bug fixes!
<sub>Jul 5, 2022</sub>
### UX
#### Added 
* **General**:
  * **r!compliment**: You can now get jusi compliments from the bot! (thank you pigon!)

#### Changed
* **General**:
  * **r!pic**: you can now request only one person's pics! (thank you kwan!)

#### Fixed
* **temp_task loop**: When CPU temp got too high, bot would loop the warning message
* **`r!report` pointing toward kwanCore**
* **Sysinfo format bug**
* **scsearch bug**: Soundcloud would autocorrect to youtube sometimes
* **`r!uwu` always off bug**
* **jus-just bug**: Just would trigger the `jus`-responses


## v3.0 - kwanCore UPDATE!!!
<sub>May 8, 2022</sub>
### UX
#### Added
* **Bot Info**:
  * **r!sysinfo**: is like `r!rpi` and `r!filecheck`, but much prettier in a way
* **Music**:
  * **Anti-troll stuff**: like now you can't skip someone else's song from another vc
  * **r!play**: SoundCloud integration! 
    * you can use the `--soundcloud` or `-sc` flag to use SoundCloud for your searches
  * **r!remove**: you can remove a song from the queue in advance
  * **r!lyrics**: you can get the lyrics to the currently playing song through Genius.com
* **Memes**: EPIC MEMES AND STUFF
  * **r!memes**: get the freshest memes from r/memes and r/dankmemes
  * **r!tifu**: watch people fuck up badly on today's episode of `Today I Fucked Up..`
  * **r!wholesome**: get some comfy wholesome vibes from r/wholesomememes and r/comfypasta
  * **r!shitpost**: get some liquid diarrhea humor, straight from r/shitposting, r/skamtebord, r/surrealmemes, and r/196
  * **r!meirl**: `oh shit dat me, he just like me frfr` moments from r/me_irl, r/discord_irl, and r/me_irlgbt
  * **r!tumblr**: for when you need to look at a tumblr post, from reddit, through discord.
  * **r!urban**: search Urban Dictionary for a totally not cursed word
  
#### Changed
* **General**:
  * **Cooldowns**: cooldowns are user-based, instead of server-based now
  * **r!uwu**: chances of getting an image instead of text has been raised to 50% from the previous 42%
* **Music**: 
  * **Embeds**: have been replaced with cooler responses
  * **Inactivity**: bot now checks for inactivity in a way smarter way
  * **r!cum**: instead of queuing three different files, it queues one file with the whole cum trilogy
  * **r!queue**: 
    * it indicates the currently playing song
    * it displays the length of files queued via `r!playfile` correctly now
* **DevTools**: every settings command has been merged into ->
  * **r!settings**: you can change every settings from a singular command
* **Help**:
  * **r!help**: you can get help for a specific command now!
* **Status**: the status message now changes every 10 minutes
 
#### Removed
* **Music**:
  * **r!playlocal**: why would we need it when `r!playfile` works
  * **r!songlist**: dumb dumb poopie
* **DevTools**:
  * you can no longer log custom messages
  * **r!devtools**: the help command has been merged into `r!help`
  * **r!newlog**: you can create a new log file by using the `--create-new` or `-n` flag on `r!log`


### Code
#### Added
* **Linting**: The code is now 34% cleaner! Thanks to kwanCore!
* **Logging**: very cool logging with `shortcuts.easylogger`

#### Changed
* Directory structure
  * `bot/assets` -> `bot/usercontent`
    * `bot/assets/*` -> `bot/*`
  * `bot/bot.py` -> `bot/main.py`
* Moved all the custom responses into a yaml file for easier changes
* Made the error_handling more efficient by just printing the errors
* Removed the config check from every file, and instead passed it through the `self.bot` object


### Misc
#### Added
* Official [kwanBot logo](https://github.com/dopebnan/kwanbot/blob/main/assets/logo.png).
#### Changed
* Instead of `Mozilla Public License 2.0`, kwanBot is now licensed under `GNU General Public License v3`
* `README.md` got a HEAVY update
* Reformatted the changelog

## v2.3.1 
### Every version below v3.0 can be found in the [old changelog](https://github.com/dopebnan/kwanbot/blob/main/.old.changelog.md)
