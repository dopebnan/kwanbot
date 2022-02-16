import json
import os
import platform
import time

from discord.ext.commands.errors import BadArgument

from assets import shortcut, embeds

import discord
from discord.ext import commands

with open("assets/config.json") as f:
	config = json.load(f)


with open("assets/settings.json") as f:
	settings = json.load(f)


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

devJSON = {
	"tag": "Dev",
	"settingsVer": f"{version['VERSION']}",
	"picCooldown": 5,
	"picReturn": True,
	"autopic": True,
	"autopicCooldown": 5,
	"autopicSleep": 5,
	"autopicReturn": True,
	"uwu": True,
	"uwuCooldown": 5,
	"uwuReturn": True,
	"painCooldown": 5,
	"painReturn": True
}

defaultJSON_obj = json.dumps(defaultJSON, indent=2)
devJSON_obj = json.dumps(devJSON, indent=2)


class DevTools(commands.Cog, name="devtools"):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name="filecheck", aliases=["dskchk", "chkdsk", "syscheck", "fsck"])
	@commands.has_role("devtools")
	async def filecheck(self, context):
		# Reloading settings.json in case it had any changes
		with open("assets/settings.json") as file:
			global settings
			setting = json.load(file)

		pic_num = str(len(os.listdir("./assets/img/pic"))) if os.path.isdir("./assets/img/pic") else 0
		uwu_num = str(len(os.listdir("./assets/img/uwu"))) if os.path.isdir("./assets/img/pic") else 0

		embed = discord.Embed(title="filecheck", color=0x2000DF)
		embed.add_field(name="r!pic Images:", value=f"`{pic_num}`")
		embed.add_field(name="r!uwu Images:", value=f"`{uwu_num}`")
		embed.add_field(name="settings.json Tag:", value=f"`# {setting['tag']}`", inline=False)
		embed.add_field(name="settings.json Version:", value=f"`{setting['settingsVer']}`")
		embed.add_field(name="Version:", value=f"`{version['VERSION']}`")
		embed.add_field(name="DevTools Version:", value=f"`{version['DEVTOOLVER']}`")
		embed.add_field(name="ID:", value=f"`{self.bot.user.id}`", inline=False)
		embed.add_field(name="API Version:", value=f"`{discord.__version__}`")
		embed.add_field(name="Python Version:", value=f"`{platform.python_version()}`")
		osys = '-'.join(platform.platform().split('-', 2)[0:2])
		embed.add_field(name="Operating System:", value=f'`{osys}`')
		embed.add_field(name="Time Since Last Update", value=f"<t:{version['lastUpdate']}:R>", inline=False)
		embed.set_footer(text="vibecheck")

		await context.send(embed=embed)

	@commands.command(name="reset", aliases=["default"])
	@commands.has_role("devtools")
	async def reset(self, context):
		with open("assets/settings.json", 'w') as file:
			file.write(defaultJSON_obj)
		with open("assets/settings.json") as file:
			global settings
			settings = json.load(file)

		embed = discord.Embed(
			title="Reset settings.json to default",
			color=0x0C8708
		)
		await context.send(embed=embed)

	@commands.command(name="debug", aliases=["debugmode", "devmode", "developermode"])
	@commands.has_role("devtools")
	async def debug(self, context):
		# Replace settings.json with the dev settings
		with open("assets/settings.json", 'w') as file:
			file.write(devJSON_obj)
		with open("assets/settings.json") as file:
			global settings
			settings = json.load(file)

		embed = discord.Embed(
			title="settings.json in DebugMode",
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
	@commands.has_role("devtools")
	async def log(self, context, *args):

		arg = "".join(args)
		
		if arg == "":
			user = context.message.author
			log = discord.File("./logs/log.txt")

			await user.send("Here's the log", file=log)	
			await context.send("Check DMs")
		
		else:
			shortcut.logging(context.message, arg, skip=True)
			await context.send(embed=discord.Embed(title="Comment logged successfully", color=0x0C8708))

	@commands.command(name="newlog", aliases=["deletelog", "fucklog"])
	@commands.has_role("devtools")
	async def newlog(self, context):
		os.rename("./logs/log.txt", f"./logs/log{int(time.time())}.txt")
		with open("./logs/log.txt", 'a') as file:
			file.write(f"\nLOG\n----{int(time.time())}----\n")

		embed = discord.Embed(title="Created a new log.txt!", color=0x0C8708)
		await context.send(embed=embed)

	@commands.command(name="picDev")
	@commands.has_role("devtools")
	async def pic_dev(self, context, delim=None, value=None):
		if value is not None and value.isnumeric():
			value = int(value)
		elif delim is not None:
			raise BadArgument
		
		if delim == "Cooldown":
			settings["picCooldown"] = value
		
		elif delim == "Return":
			settings["picReturn"] = bool(value)
		
		else:
			foo = 1
		
		if "foo" in locals():
			embed = discord.Embed(title="DevTools", description="r!pic values", color=0x8000B2)
			embed.add_field(name="picCooldown:", value=f"{settings['picCooldown']}")
			embed.add_field(name="picReturn", value=f"{settings['picReturn']}")
			embed.set_footer(text="nerdshit")
			
			await context.send(embed=embed)
		
		else:
			settings["tag"] = "Custom"
			with open("assets/settings.json", 'w') as file:
				json.dump(settings, file, indent=2)

			embed = embeds.successful_save()
			await context.send(embed=embed)

	@commands.command(name="painDev")
	@commands.has_role("devtools")
	async def pain_dev(self, context, delim=None, value=None):
		if value is not None and value.isnumeric():
			value = int(value)
		elif delim is not None:
			raise BadArgument
		
		if delim == "Cooldown":
			settings["painCooldown"] = value
		
		elif delim == "Return":
			settings["painReturn"] = bool(value)
		
		else:
			foo = 1
		
		if "foo" in locals():
			embed = discord.Embed(title="DevTools", description="r!pain values", color=0x8000B2)
			embed.add_field(name="painCooldown:", value=f"{settings['painCooldown']}")
			embed.add_field(name="painReturn", value=f"{settings['painReturn']}")
			embed.set_footer(text="nerdshit")
			
			await context.send(embed=embed)
		
		else:
			settings["tag"] = "Custom"
			with open("assets/settings.json", 'w') as file:
				json.dump(settings, file, indent=2)

			embed = embeds.successful_save()
			await context.send(embed=embed)
	
	@commands.command(name="autoDev")
	@commands.has_role("devtools")
	async def auto_dev(self, context, delim=None, value=None):
		if value is not None and value.isnumeric():
			value = int(value)
		elif delim is not None:
			raise BadArgument
		
		if delim == "Switch":
			settings["autopic"] = bool(value)

		elif delim == "Sleep":
			settings["autopicSleep"] = value
			settings["autopicCooldown"] = value * 4
		
		elif delim == "Return":
			settings["autopicReturn"] = bool(value)
		
		else:
			foo = 1
		
		if "foo" in locals():
			embed = discord.Embed(title="DevTools", description="r!autopic values", color=0x8000B2)
			embed.add_field(name="autopic:", value=f"{settings['autopic']}")
			embed.add_field(name="autopicCooldown", value=f"{settings['autopicCooldown']}")
			embed.add_field(name="autopicSleep:", value=f"{settings['autopicSleep']}")
			embed.add_field(name="autopicReturn", value=f"{settings['autopicReturn']}")
			embed.set_footer(text="nerdshit")
			await context.send(embed=embed)

		else:
			settings["tag"] = "Custom"
			with open("assets/settings.json", 'w') as file:
				json.dump(settings, file, indent=2)
			
			embed = embeds.successful_save()
			await context.send(embed=embed)
		
	@commands.command(name="uwuDev")
	@commands.has_role("devtools")
	async def uwu_dev(self, context, delim=None, value=None):
		if value is not None and value.isnumeric():
			value = int(value)
		elif delim is not None:
			raise BadArgument

		if delim == "Switch":
			settings["uwu"] = bool(value)

		elif delim == "Cooldown":
			settings["uwuCooldown"] = value
		
		elif delim == "Return":
			settings["uwuReturn"] = bool(value)
		
		else:
			foo = 1

		if "foo" in locals():
			embed = discord.Embed(title="DevTools", description="r!uwu values", color=0x8000B2)
			embed.add_field(name="uwu", value=f"{settings['uwu']}")
			embed.add_field(name="uwuCooldown", value=f"{settings['uwuCooldown']}")
			embed.add_field(name="uwuReturn", value=f"{settings['uwuReturn']}")
			embed.set_footer(text="nerdshit")
			await context.send(embed=embed)
		
		else:
			settings["tag"] = "Custom"
			with open("assets/settings.json", 'w') as file:
				json.dump(settings, file, indent=2)
			
			embed = embeds.successful_save()
			await context.send(embed=embed)


def setup(bot):
	bot.add_cog(DevTools(bot))
