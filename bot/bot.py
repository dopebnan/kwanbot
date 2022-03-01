import json
import os.path
import sys
import random
import unicodedata
import time
import asyncio
import subprocess

from assets import shortcut, embeds


import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot

gloriReply = ["glori tu mother feeshland komrad o7", "glorious day, comrade o7", "glori glori", "glori comrade o7"]
jusReply = ["<:jus:884844071766622258>", "<:bussy:884844071615594506><:jus:884844071766622258>",
            "<:pigon:884844071644966972>" * 3 + "<:jus:884844071766622258>",
            "pigon be walkin' doe", "al hal ze jus", "pigon pog", "bot pog", "bnan pog",
            "ze gretest, ze best, ze jusiest", "jus zon"]
badReply = ["sorryyy", "noted.", "no u", ":(", "fuck you, ***bitch***", "i will commit toaster", "i will commit toe",
            "i will commit battery"]
goodReply = ["you are very yes", "hel ye", "pogpogpog", "poggers", "<:pogfield:884844071733055488>"]

onCooldown = ["Slow down there buckaroo", "not so fast", "stop", "cooldown be poopin' them parties", "cooldown rule",
              "no.", "anti-spam caught yo ass"]
missingArgPix = ["HOW MANY TIMES???", "you forgot the part where number", "where number", "HOW MANY PICS???",
                 "you need to give me a number too smh", "me need number innit"]
status = ["r!help", "I'm gonna shit yourself", "bot be poggin'", "nope, it was just penis", "pigon be walkin' doe",
          "innit", "pee is coming out of my eyes", "raid shadow leg", "nipple crippling", "decreasing molesting rates",
          "slicing foreskin", "peeing from balls", "cancelling global warming", "have hair in your food", "shiddin'",
          "lock meself outta the fridge", "OH NO! BUSSY BROKEN!", "who fucked oil", "transparent nutrient",
          "ALPHA SHITTING", "ratio + bald goku", "DO NOT FUCK SHIT"]

# File checks and json opening
if not os.path.isfile("assets/version.json"):
    sys.exit("version.json not found.")
else:
    with open("assets/version.json") as f:
        version = json.load(f)

defaultJSON = {
    "tag": "Default-auto",
    "settingsVer": f"{version['VERSION']}",
    "picCooldown": 30,
    "picReturn": False,
    "autopic": False,
    "autopicSleep": 15,
    "autopicCooldown": 60,
    "autopicReturn": False,
    "uwu": False,
    "uwuCooldown": 15,
    "uwuReturn": True,
    "painCooldown": 15,
    "painReturn": False
}

defaultJSON_obj = json.dumps(defaultJSON, indent=2)

if not os.path.isfile("assets/config.json"):
    sys.exit(f"config.json not found. (dir: {os.path})")
else:
    with open("assets/config.json") as f:
        config = json.load(f)

if not os.path.isdir("./logs/"):
    os.mkdir("./logs")

if not os.path.isfile("assets/settings.json"):
    with open("assets/settings.json", "w") as f:
        f.write(defaultJSON_obj)
else:
    with open("assets/settings.json") as f:
        settings = json.load(f)

intents = discord.Intents.default()

bot = Bot(command_prefix="r!", intents=intents)

bot.version = version
bot.temp_warning = 0


@bot.event
async def on_ready():
    print(f"        Kwanbot!\n    API ver: {discord.__version__}\n    bot: {bot.user.name}\n\n\n")
    with open("./logs/log.txt", 'a') as file:
        file.write(f"\nLOG\n----{int(time.time())}----\n")
    status_task.start()
    temp_task.start()


@tasks.loop(minutes=6)
async def status_task():
    await bot.change_presence(activity=discord.Game(random.choice(status)))
    print("\nChanged status message.\n")


@tasks.loop(minutes=5)
async def temp_task():
    await bot.wait_until_ready()
    id_list = []
    for ID in config["warningChannel"]:
        id_list.append(bot.get_channel(ID))
    try:
        temp = float(shortcut.terminal("vcgencmd measure_temp").split('=', 1)[1].split("'", 1)[0])
    except subprocess.CalledProcessError:
        temp = 69
    if temp > 65:
        bot.temp_warning += 1

    if 0 < bot.temp_warning < 5:
        embed = discord.Embed(title="WARNING", description=f"the pi's temp is `{temp}'C`", color=0xffc300)
        embed.set_footer(text=f"{bot.temp_warning}. warning")
        shortcut.logging(error_msg=f"WARN: the CPU is at {temp}'C", raw=True)
        for channel in id_list:
            await channel.send(embed=embed)
    elif bot.temp_warning > 5:
        bot.temp_warning = 0
        embed = discord.Embed(title="STOPPING", description=f"the pi's temp is `{temp}'C`", color=0xcc3300)
        embed.set_footer(text=f"last warning")
        shortcut.logging(error_msg=f"CRITICAL: the CPU is at {temp}'C", raw=True)
        for channel in id_list:
            await channel.send(embed=embed)
        await reload(1)

bot.remove_command("help")
if __name__ == "__main__":
    pass

bot.load_extension('cogs.help')
bot.load_extension('cogs.general')
bot.load_extension('cogs.devtools')
bot.load_extension('cogs.gruvi')


async def reload(sleep):
    print("reloading")
    await asyncio.sleep(sleep)
    bot.reload_extension("cogs.help")
    bot.reload_extension("cogs.general")
    bot.reload_extension("cogs.devtools")
    bot.reload_extension("cogs.gruvi")
    with open("assets/version.json") as file:
        bot.version = json.load(file)


@bot.event
async def on_command_completion(ctx):
    cmd = ctx.command.qualified_name
    if not cmd == "pic" and not cmd == "log":
        shortcut.logging(ctx.message)

    if cmd.endswith("Dev"):
        await reload(1)
    elif cmd == "update":
        await reload(6)
        await ctx.send(f"    current version: `{bot.version['VERSION']}`")


@bot.event
async def on_command_error(context, error):
    cmd = context.command.qualified_name if context.command else context.command

    x = True
    errormsg = str(error).replace("Command raised an exception: ", '')

    if isinstance(error, commands.CommandOnCooldown):
        seconds = round(error.retry_after)

        embed = discord.Embed(
            title=f"{onCooldown[random.randint(0, len(onCooldown) - 1)]}",
            description=f"***{seconds}s** left of cooldown. wait.*",
            color=0x4361EE
        )

    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="That command doesn't exist, dummy",
            description="better luck next time",
            color=0xE3170A
        )

    elif isinstance(error, commands.BadArgument):
        if cmd == "playfile":
            embed = discord.Embed(
                title="Wrong filetype",
                description="It has to be an audio file, dumbass",
                color=0xE3170A
            )
            embed.set_footer(text="preferably an mp3")
        else:
            embed = embeds.error_type()

    elif isinstance(error, commands.MissingRequiredArgument):
        if cmd == "autopic":
            embed = discord.Embed(
                title=f"{missingArgPix[random.randint(0, len(missingArgPix) - 1)]}",
                description="it's *r!autopic* ***number***, you dumbass",
                color=0xE3170A
            )

        else:
            embed = discord.Embed(
                title=f"MissingRequiredArgument",
                color=0xE3170A
            )

    elif isinstance(error, TypeError):
        if cmd == "playfile":
            embed = discord.Embed(
                title="I can't play that",
                description="CUZ YOU DIDNT GIVE ME A FILE, DUMBASS",
                color=0xE3170A
            )

    elif isinstance(error, commands.MissingAnyRole):
        embed = embeds.error_missing_role()

    elif isinstance(error, AttributeError):
        embed = embeds.author_not_in_vc()

    elif isinstance(error.original, ConnectionError):
        embed = embeds.error_ytdl()

    elif isinstance(error.original, discord.errors.InvalidArgument):
        embed = embeds.error_invalid_arg(f"r!{context.command.qualified_name}")

    else:
        # ostrich algorithm
        if cmd == "cum":
            shortcut.logging(context.message, error)
            x = False
        else:
            errormsg_split = errormsg.split(':', 1)
            embed = discord.Embed(title=errormsg_split[0], description=errormsg_split[1], color=0xE3170A)
            embed.set_footer(text="sorry, tell bnan")

    print(error)
    if x:
        await context.send(embed=embed)
        shortcut.logging(context.message, errormsg)

        raise error


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = unicodedata.normalize('NFKD', message.content.casefold())

    if 'jus ' in msg or 'jus' in msg and 'just' not in msg:
        await message.channel.send(random.choice(jusReply))

    elif 'glori' in msg:
        await message.channel.send(random.choice(gloriReply))

    elif msg == 'bad bot':
        await message.channel.send(random.choice(badReply))

    elif msg == "good bot" or msg == "gud bot":
        await message.channel.send(random.choice(goodReply))

    await bot.process_commands(message)


bot.run(config["TOKEN"])
