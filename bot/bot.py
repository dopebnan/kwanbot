import json
import os.path
import sys
import random
import unicodedata
import time

from shortcut import Shortcut

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot

gloriReply = ["glori tu mother feeshland komrad o7", "glorious day, comrade o7", "glori glori", "glori comrade o7"]
jusReply = ["<:jus:884844071766622258>", "<:bussy:884844071615594506><:jus:884844071766622258>", "<:pigon:884844071644966972><:pigon:884844071644966972><:pigon:884844071644966972><:jus:884844071766622258>", "pigon be walkin doe", "al hal ze jus", "pigon pog", "bot pog", "bnan pog", "ze gretest, ze best, ze jusyest", "jus zon"]
badReply = ["sorryyy", "noted.", "no u", ":(", "fuck you, ***bitch***", "i will commit toaster", "i will commit toe", "i will commit battery"]
goodReply = ["you are very yes", "hel ye", "pogpogpog", "poggers", "<:pogfield:884844071733055488>"]

status = ["r!help", "I'm gonna shit yourself", "bot be poggin", "omnibussy pog", "nope, it was just penis", "pigon be walkin doe", "glori comrade", "innit", "Ah yes, anti-bussyn't fancy water", "kwan isn't britain", "pee is coming out of my eyes", "raid shadow leg", "nipple crippling", "decreasing molesting rates", "slicing foreskin", "peeing from balls", "cancelling global warming", "have hair in your food", "finna bust out the thighstash", ""]

if not os.path.isfile("assets/config.json"):
	sys.exit("config.json not found.")
else:
	with open("assets/config.json") as f:
		config = json.load(f)

if not os.path.isdir("./logs/"):
	os.mkdir("./logs")

if not os.path.isfile("assets/settings.json"):
	sys.exit("settings.json not found.")
else:
	with open("assets/settings.json") as f:
		settings = json.load(f)

onCooldown = ["Slow down there buckaroo", "not so fast", "stop", "cooldown be poopin them parties", "cooldown rule", "no.", "anti-spam caught yo ass"]
missingArgPix = ["HOW MANY TIMES???", "you forgot the part where number", "where number", "HOW MANY PICS???", "you need to give me a number too smh", "me need number innit"]

intents = discord.Intents.default()

bot = Bot(command_prefix="r!", intents=intents)

@bot.event
async def on_ready():
	print(f"        Kwanbot!\n    API ver: {discord.__version__}\n    bot: {bot.user.name}\n\n\n")
	with open("./logs/log.txt", 'a') as f:
		f.write(f"\nLOG\n----{int(time.time())}----\n")
	status_task.start()
	
@tasks.loop(minutes=6.0)
async def status_task():
	await bot.change_presence(activity=discord.Game(random.choice(status)))
	print("\nChanged status message.\n")

bot.remove_command("help")
if __name__ == "__main__":
	bot.load_extension('cogs.general')
	bot.load_extension('cogs.devtools')

@bot.event
async def on_command_completion(ctx):
	if not ctx.command.qualified_name == "pic":
		Shortcut().logging(ctx.message)

@bot.event
async def on_command_error(context, error):
	if isinstance(error, commands.CommandOnCooldown):
		seconds = divmod(error.retry_after, 60)[1]

		embed = discord.Embed(
			title=f"{onCooldown[random.randint(0, len(onCooldown) - 1)]}",
			description=f"***{round(seconds)}s** left of cooldown. wait.*",
			color=0x4361EE
		)
		await context.send(embed = embed)

	elif isinstance(error, commands.MissingRequiredArgument):
		if context.command.qualified_name == "autopic":

			embed = discord.Embed(
				title=f"{missingArgPix[random.randint(0, len(missingArgPix) - 1)]}",
				description="it's *r!autopic* ***number***, you dumbass",
				color=0xE3170A
			)
			await context.send(embed=embed)
			Shortcut().logging(context.message, "r!autopic missing number")

		else:
			embed = discord.Embed(
				title=f"MissingRequiredArgument",
				color=0xE3170A
			)
			await context.send(embed=embed)
			Shortcut().logging(context.message, f"Missing arguments")
	
	elif isinstance(error, commands.BadArgument):
		if context.command.qualified_name == "autoDev":
			try:
				msg = context.message.content.split(" ", 2)[2]
			except IndexError:
				msg = None

			ftype = Shortcut().fileType(msg)

			if context.message.content.startswith("r!autoDev Switch") or context.message.content.startswith("r!auto Return"):
				embed = Shortcut.Embeds().TypeErrorEmbed("boolean", ftype)
				Shortcut().logging(context.message, f"Invalid arguments")

			elif context.message.content.startswith("r!autoDev Sleep"):
				embed = Shortcut.Embeds().TypeErrorEmbed("integer", ftype)		
				Shortcut().logging(context.message, "Invalid arguments")

			else:
				embed = Shortcut.Embeds().InvalidArgumentError(context.command.qualified_name)				
				Shortcut().logging(context.message, "Invalid arguments")
			
			await context.send(embed=embed)
		
		elif context.command.qualified_name == "picDev":
			try:
				msg = context.message.content.split(" ", 2)[2]
			except IndexError:
				msg = None
			
			arg = context.message.content.split(" ", 2)[1]
			ftype = Shortcut().fileType(msg)

			if arg == "Cooldown":
				embed = Shortcut().Embeds().TypeErrorEmbed("integer", ftype)
			elif arg == "Return":
				embed = Shortcut().Embeds().TypeErrorEmbed("boolean", ftype)
			else:
				embed = Shortcut().Embeds().InvalidArgumentError("r!picDev")
			
			await context.send(embed=embed)
			Shortcut().logging(context.message, "TypeError")

		else:
			embed = Shortcut.Embeds().InvalidArgumentError(f"r!{context.command.qualified_name}")
			await context.send(embed=embed)
			Shortcut().logging(context.message, "Invalid arguments")
	
	elif isinstance(error, commands.MissingAnyRole):
		embed = Shortcut.Embeds().MissingRoleError()
		await context.send(embed=embed)
	
	elif isinstance(error, commands.CommandNotFound):
		embed = discord.Embed(
			title="That command doesn't exist, dummy",
			description="better luck next time",
			color=0xE3170A
		)
		await context.send(embed=embed)
		Shortcut().logging(context.message, "Command not found")

	else:
		embed = Shortcut.Embeds().GenericError()
		await context.send(embed=embed)
		Shortcut().logging(context.message, "Unknown Error")

	# disabled for nicer command window view
	raise error

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	
	msg = unicodedata.normalize('NFKD', message.content.casefold())

	if 'jus ' in msg or 'jus' in msg and 'just' not in msg:
		await message.channel.send(random.choice(jusReply))
	
	elif 'glori' in msg:
		if not message.author.id in config["uwuIDs"]:
			await message.channel.send(random.choice(gloriReply))
		else:
			await message.channel.send(random.choice(["something isn't right", "WE GOT A WESTERN SPY HERE BOIS", "..fake commie..", "this fucking cappy smh", "cappy bullshit"]))

	elif msg == 'bad bot':
		await message.channel.send(random.choice(badReply))
	
	elif msg == "good bot" or msg == "gud bot":
		await message.channel.send(random.choice(goodReply))
	
	elif msg == "sorry bot":
		await message.channel.send(">:C")

	await bot.process_commands(message)




bot.run(config["TOKEN"])
