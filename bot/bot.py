import json
import os.path
import sys
import random
import unicodedata
import time

from assets import shortcut, embeds

# TODO: move bugs to github
# TODO: linux

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot

gloriReply = ["glori tu mother feeshland komrad o7", "glorious day, comrade o7", "glori glori", "glori comrade o7"]
jusReply = ["<:jus:884844071766622258>", "<:bussy:884844071615594506><:jus:884844071766622258>",
			"<:pigon:884844071644966972><:pigon:884844071644966972><:pigon:884844071644966972><:jus:884844071766622258>",
			"pigon be walkin' doe", "al hal ze jus", "pigon pog", "bot pog", "bnan pog", "ze gretest, ze best, ze jusiest",
			"jus zon"]
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
			"ALPHA SHITTING", "ratio + bald goku", "DO NOT FUCK SHIT", "PADORU PADORUUU"]

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


@bot.event
async def on_ready():
	print(f"        Kwanbot!\n    API ver: {discord.__version__}\n    bot: {bot.user.name}\n\n\n")
	with open("./logs/log.txt", 'a') as file:
		file.write(f"\nLOG\n----{int(time.time())}----\n")
	status_task.start()
	

@tasks.loop(minutes=6.0)
async def status_task():
	await bot.change_presence(activity=discord.Game(random.choice(status)))
	print("\nChanged status message.\n")

bot.remove_command("help")
if __name__ == "__main__":
	print("ASd")

bot.load_extension('cogs.help')
bot.load_extension('cogs.general')
bot.load_extension('cogs.devtools')
bot.load_extension('cogs.gruvi')


@bot.event
async def on_command_completion(ctx):
	if ctx.command.qualified_name == "log":
		pass  # Unneeded, but makes log look nicer
	if not ctx.command.qualified_name == "pic" and not ctx.command.qualified_name == "log":
		shortcut.logging(ctx.message)
	
	
@bot.event
async def on_command_error(context, error):
	x = True

	if isinstance(error, commands.CommandOnCooldown):
		seconds = round(error.retry_after)

		embed = discord.Embed(
			title=f"{onCooldown[random.randint(0, len(onCooldown) - 1)]}",
			description=f"***{seconds}s** left of cooldown. wait.*",
			color=0x4361EE
		)

	elif isinstance(error, commands.MissingRequiredArgument):
		if context.command.qualified_name == "autopic":
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
	
	elif isinstance(error, commands.BadArgument):
		embed = embeds.error_type()
	
	elif isinstance(error, discord.InvalidArgument):
		embed = embeds.error_invalid_arg(f"r!{context.command.qualified_name}")
	
	elif isinstance(error, commands.MissingAnyRole):
		embed = embeds.error_missing_role()
	
	elif isinstance(error, commands.CommandNotFound):
		embed = discord.Embed(
			title="That command doesn't exist, dummy",
			description="better luck next time",
			color=0xE3170A
			)

	elif isinstance(error, AttributeError):
		embed = embeds.author_not_in_vc()

	else:
		# ostrich algorithm
		if context.command.qualified_name == "cum":
			shortcut.logging(context.message, error)
			x = False
		else:	
			embed = embeds.unknown_error()
		
	print(error)
	if x:
		await context.send(embed=embed)
		shortcut.logging(context.message, type(error))

		raise error


@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	
	msg = unicodedata.normalize('NFKD', message.content.casefold())

	if 'jus ' in msg or 'jus' in msg and 'just' not in msg:
		await message.channel.send(random.choice(jusReply))
	
	elif 'glori' in msg:
		if message.author.id not in config["uwuIDs"]:
			await message.channel.send(random.choice(gloriReply))
		else:
			await message.channel.send(random.choice(["something isn't right", "WE GOT A WESTERN SPY HERE BOIS",
														"..fake commie..", "this fucking cappy smh", "cappy bullshit"]))

	elif msg == 'bad bot':
		await message.channel.send(random.choice(badReply))
	
	elif msg == "good bot" or msg == "gud bot":
		await message.channel.send(random.choice(goodReply))

	await bot.process_commands(message)


bot.run(config["TOKEN"])
