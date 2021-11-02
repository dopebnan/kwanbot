import json
import os
import platform
import sys
import time

from shortcut import Shortcut

import discord
from discord.ext import commands



# TODO: Finish the autoupdate thingy, if possible
'''
GitHub doesn't have good autoupdate stuff, be aware
'''



if not os.path.isfile("assets/config.json"):
	sys.exit("config.json not found.")
else:
	with open("assets/config.json") as f:
		config = json.load(f)


if not os.path.isfile("assets/settings.json"):
	sys.exit("settings.json not found.")
else:
	with open("assets/settings.json") as f:
		settings = json.load(f)

defaultJSON = {
	"tag": "Default-auto",
	"settingsVer": f"{config['VERSION']}",
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

devJSON = {
  "tag": "Dev",
  "settingsVer": f"{config['VERSION']}",
  "picCooldown": 5,
  "picReturn": True,
  "autopic": True,
  "autopicCooldown": 5,
  "autopicSleep": 5,
  "autopicReturn": True,
  "uwu": True,
  "uwuCooldown": 5,
  "uwuReturn": True,
  "painCooldown": 15,
  "painReturn": False
}

defaultJSON_obj = json.dumps(defaultJSON, indent=2)
devJSON_obj = json.dumps(devJSON, indent=2)



class DevTools(commands.Cog, name="devtools"):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name="filecheck", aliases=["dskchk", "chkdsk", "syscheck", "fsck"])
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def filecheck(self, context):
		# Reloading settings.json in case it had any changes
		with open("assets/settings.json") as f:
			settings = json.load(f)

		picNums = str(len(os.listdir("./assets/img/pic")))
		uwuNums = str(len(os.listdir("./assets/img/uwu")))

		embed = discord.Embed(
			title="filecheck",
			color=0x2000DF
		)
		embed.add_field(
			name="r!pic Images:",
			value=f"`{picNums}`"
		)
		embed.add_field(
			name="r!uwu Images:",
			value=f"`{uwuNums}`"
		)
		embed.add_field(
			name="settings.json Tag:",
			value=f"`# {settings['tag']}`",
			inline=False
		)
		embed.add_field(
			name="settings.json Version:",
			value=f"`{settings['settingsVer']}`"
		)
		embed.add_field(
			name="Version:",
			value=f"`{config['VERSION']}`",
		)
		embed.add_field(
			name="DevTools Version:",
			value=f"`{config['DEVTOOLVER']}`",
		)
		embed.add_field(
			name="ID:",
			value=f"`{self.bot.user.id}`",
			inline=False
		)
		embed.add_field(
			name="API Version:",
			value=f"`{discord.__version__}`"
		)
		embed.add_field(
			name="Python Version:",
			value=f"`{platform.python_version()}`"
		)
		embed.add_field(
			name="Time Since Last Update",	
			value=f"<t:{config['lastUpdate']}:R>",
			inline=False
		)
		embed.set_footer(text="vibecheck")

		await context.send(embed=embed)

	@commands.command(name="reset", aliases=["default"])
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def reset(self, context):
		try:
			# Replace settings.json with the default settings
			with open("assets/settings.json", 'w') as f:
				f.write(defaultJSON_obj)
		except:
			embed = discord.Embed(
				title="An error occurred while resetting",
				description="sucks to be you",
				color=0xE3170A
			)
			await context.send(embed=embed)
		else:
			embed = discord.Embed(
				title="Reset settings.json to default",
				color=0x0C8708
			)
			await context.send(embed=embed)

	@commands.command(name="debug", aliases=["debugmode", "devmode", "developermode"])
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def debug(self, context):
		try:
			# Replace settings.json with the dev settings
			with open("assets/settings.json", 'w') as f:
				f.write(devJSON_obj)
		except:
			embed = discord.Embed(
				title="An error occurred",
				description="how??",
				color=0xE3170A
			)
			await context.send(embed=embed)
		else:
			embed = discord.Embed(
				title="settings.json in DebugMode",
				description="Do a r!reload for changes to take effect",
				color=0x0C8708
			)
			await context.send(embed=embed)
	
	@commands.command(name="sourcecode", aliases=["gh", "code", "source", "github"])
	async def sourcecode(self, context):
		embed = discord.Embed(
			title="Source-code",
			description="You can view the source code [here](https://github.com/dopebnan/kwanbot)",
			color=0xA000A4
		)
		await context.send(embed=embed)

	@commands.command(name="log", aliases=["dmlog", "logs", "givlog", "wood"])
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def log(self, context, *args):

		arg = "".join(args)
		
		if arg == "":
			user = context.message.author
			log = discord.File("./logs/log.txt")

			await user.send("Here's the log", file=log)	
			await context.send("Check DMs")
		
		else:
			Shortcut().logging(context.message, arg)

			await context.send(embed=discord.Embed(title="Comment logged successfully", color=0x0C8708))

	@commands.command(name="newlog", aliases=["deletelog", "fucklog"])
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def newlog(self, context):
		os.rename("./logs/log.txt", f"./logs/log{int(time.time())}.txt")
		with open("./logs/log.txt", 'a') as f:		
			f.write(f"\nLOG\n----{int(time.time())}----\n")
		
		embed = discord.Embed(title="Created a new log.txt!", color=0x0C8708)
		await context.send(embed=embed)

	@commands.command(name="picDev")
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def picDev(self, context, delim: str=None, value=None):
		# anyone could do this better, but eh fuck it, it works
		if delim == "Cooldown":
			try:
				value = int(value)
				settings["picCooldown"] = value
			except:
				raise commands.BadArgument
		
		elif delim == "Return":
			if value in ["False", "0"]:
				value = False
			elif value in ["True", "1"]:
				value = True
			else:
				raise commands.BadArgument
			settings["picReturn"] = value
		
		elif delim == None:
			x = True	
		else:
			raise commands.BadArgument
			
		try:
			x = x
		except:
			x = None
		
		if x:
			embed = discord.Embed(
				title="DevTools",
				description="r!pic values",
				color=0x8000B2
			)
			embed.add_field(
				name="picCooldown:",
				value=f"{settings['picCooldown']}"
				)
			embed.add_field(
				name="picReturn",
				value=f"{settings['picReturn']}"
				)
			embed.set_footer(text="nerdshit")
			await context.send(embed=embed)
		
		else:
			settings["tag"] = "Custom"
			with open("assets/settings.json", 'w') as f:
				json.dump(settings, f, indent=2)

			embed = Shortcut.Embeds.SuccessfulEmbeds().SavingComplete()
			await context.send(embed=embed)
	
	@commands.command(name="autoDev")
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def autoDev(self, context, delim: str=None, value=None):
		# anyone could do this better, but eh fuck it, it works
		if delim == "Switch":
			if value in ["False", "0"]:
				value = False
			elif value in ["True", "1"]:
				value = True
			else:
				raise commands.BadArgument
			settings["autopic"] = value

		elif delim == "Sleep":
			try:
				value = int(value)
				settings["autopicSleep"] = value 
				settings["autopicCooldown"] = value * 4
			except:
				raise commands.BadArgument

		elif delim == "Return":
			if value in ["False", "0"]:
				value = False
			elif value in ["True", "1"]:
				value = True
			else:
				raise commands.BadArgument
			settings["autopicReturn"] = value
		
		elif delim == None:
			bruh = True
		
		else:
			raise commands.BadArgument

		try:
			bruh = bruh
		except:
			bruh = None
		
		if bruh:
			embed = discord.Embed(title="DevTools",description="r!autopic values",color=0x8000B2)
			embed.add_field(name="autopic:",value=f"{settings['autopic']}")
			embed.add_field(name="autopicCooldown",value=f"{settings['autopicCooldown']}")
			embed.add_field(name="autopicSleep:",value=f"{settings['autopicSleep']}")
			embed.add_field(name="autopicReturn",value=f"{settings['autopicReturn']}")
			embed.set_footer(text="nerdshit")
			await context.send(embed=embed)
		
		else:
			settings["tag"] = "Custom"
			with open("assets/settings.json", 'w') as f:
				json.dump(settings, f, indent=2)
			
			embed = Shortcut.Embeds.SuccessfulEmbeds().SavingComplete()
			await context.send(embed=embed)
		
	@commands.command(name="uwuDev")
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def uwuDev(self, context, delim: str=None, value=None):
		# anyone could do this better, but eh fuck it, it works
		if delim == "Switch":
			if value in ["False", "0"]:
				value = False
			elif value in ["True", "1"]:
				value = True
			else:
				raise commands.BadArgument
			settings["uwu"] = value
		
		elif delim == "Cooldown":
			try:
				value = int(value)
				settings["uwuCooldown"] = value
			except:
				raise commands.BadArgument
		
		elif delim == "Return":
			if value in ["False", "0"]:
				value = False
			elif value in ["True", "1"]:
				value = True
			else:
				raise commands.BadArgument	
			settings["uwuReturn"] = value

		elif delim == None:
			x = True

		else:
			raise commands.BadArgument

		try:
			x = x
		except:
			x = None

		if x:
			embed = discord.Embed(
				title="DevTools",
				description="r!uwu values",
				color=0x8000B2
			)
			embed.add_field(
				name="uwu",
				value=f"{settings['uwu']}"
			)
			embed.add_field(
				name="uwuCooldown",
				value=f"{settings['uwuCooldown']}"
			)
			embed.add_field(
				name="uwuReturn",
				value=f"{settings['uwuReturn']}"
			)
			embed.set_footer(text="nerdshit")

			await context.send(embed=embed)
		
		else:
			settings["tag"] = "Custom"
			with open("assets/settings.json", 'w') as f:
				json.dump(settings, f, indent=2)
			
			embed = Shortcut.Embeds.SuccessfulEmbeds().SavingComplete()
			await context.send(embed=embed)

	@commands.command(name="update")
	async def update(self, context):
		pass




def setup(bot):
	bot.add_cog(DevTools(bot))
