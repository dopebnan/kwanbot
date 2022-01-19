import json
import os
import sys
import random
import asyncio

from assets import shortcut

import discord
from discord.ext import commands
from discord.ext.commands import BucketType

britCommand = ["OI LUV", "shag ye mum, das wha' I'm finna do", "ey bruv", "ey rude boi, you cool?",
				"That's rubbish, bot no do the bri'ish", "bloody brilliant, innit?", "oh bloody hell",
				"bit rewd to put da knoife in me chest innit bruv?", "OI OI OI YEAOUH WANKA WOTS OL DIS DEN",
				"bloody hell"]
succCommand = ["al hal ze bussy, al hal ze jus, al hal glorious feeshland",
				"by the light of Kwum, and the darkness of the Omnibussy, we shan't fall to cappy bullshit, comrade.",
				"May our realm look like Realm 0", "***S U C C***",
				"And with that outta the way, let's get ourselves some fermented moosucculents, shall we?",
				"Let Kwum, the Bussylords, and the Omnibussy hear our prayers. Succ ye.",
				"Let us pray to Marxboi, and the Omnibussy, comrade. Succ", "may ze omnibussy grant us greit tingz",
				"marxboi may grent uz wit jus", ]
uwuCommand = ["hwands in the aiw, this is a wobbewy!!\nPUT DA UwU's IN DA BWAG",
				"you can make my earfquake..\nbut i can make your bedrock :smirk::smirk::smirk:",
				"hey! did you just fart? :point_right::point_left:\n*cuz your blowing me away*",
				"""*roses **can** be red*
				*violets **aren't** blue* 
				*this is an actual poem*
				*in conclusion: **i'd like to rail you***
				:smirk::smirk::smirk:"""]

# Loading json files
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

if not os.path.isfile("assets/version.json"):
	sys.exit("version.json not found.")
else:
	with open("assets/version.json") as f:
		version = json.load(f)


class General(commands.Cog, name="general"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="info")
	async def info(self, context):
		embed = discord.Embed(
			title="it's ya bot",
			description="Info about bot pogpogpog",
			color=0x560BAD
		)
		embed.add_field(
			name="developed by:",
			value="programur bnan",
			inline=False
		)
		embed.add_field(
			name="version:",
			value=f'{version["VERSION"]} {version["TITLE"]}',
			inline=True
		)
		embed.add_field(
			name="DevTool version:",
			value=f"{version['DEVTOOLVER']}",
			inline=True
		)
		embed.add_field(
			name="Last update was:",
			value=f"<t:{version['lastUpdate']}:R>",
		)
		embed.set_footer(text=f"Time spent coding: 6hrs")  # TODO
		await context.send(embed=embed)

	@commands.command(name="changelog", aliases=["change", "changes", "updates"])
	async def changelog(self, context):
		file = discord.File('../changelog.md')
		await context.send(random.choice(["updates innit", "changes", "nerd shit"]), file=file)

	@commands.command(name="check", aliases=["chk"])
	async def check(self, context):
		pic_num = str(len(os.listdir("./assets/img/pic")))
		uwu_num = str(len(os.listdir("./assets/img/uwu")))

		embed = discord.Embed(
			title="check",
			color=0x4000D0
		)
		embed.add_field(
			name="r!pic images:",
			value=f"{pic_num}"
		)
		embed.add_field(
			name="r!uwu images:",
			value=f"{uwu_num}"
		)
		embed.add_field(
			name="Time since last update",
			value=f"<t:{version['lastUpdate']}:R>"
		)
		embed.set_footer(text="vibecheck")
		await context.send(embed=embed)

	@commands.command(name="ping")
	async def ping(self, context):
		embed = discord.Embed(title="reeeEEEEEEE", description=f"ping at {round(self.bot.latency * 1000)}ms", color=0x3F37C9)
		await context.send(embed=embed)

	@commands.command(name="report", aliases=["bugreport", "bug"])
	async def report(self, context):
		embed = discord.Embed(
			title="Report",
			description="To file a report, go to the [bot's page](https://github.com/dopebnan/kwanbot/issues), and open"
			" 	an issue there!",
			color=0x7209b7
		)
		await context.send(embed=embed)

	@commands.command(name="pic")
	@commands.cooldown(1, settings["picCooldown"], BucketType.guild)
	async def pic(self, context):
		pic = f'./assets/img/pic/{random.choice(os.listdir("./assets/img/pic"))}'
		msg = random.choice(["pic pog", "there ya go", "pics be like", "remember this:", "", "", "bruh"])
		await context.send(msg, file=discord.File(pic))

		if settings["picReturn"]:
			await context.send(f"*Cooldown has been set to **{settings['picCooldown']}s***")
		print(f"[r!pic] queue'd, {pic}. {msg}\n")
		shortcut.logging(context.message, f"pic: {pic}, message: {msg}")

	@commands.command(name="autopic", aliases=["pics", "pix"])
	@commands.cooldown(1, settings["autopicCooldown"], BucketType.guild)
	async def autopic(self, context, arg):
		if settings["autopic"]:
			if arg.isnumeric():
				arg = int(arg)
				if arg > 5:
					embed = discord.Embed(
						title="i legally cannot do more than 5",
						description="*pick a smaller number*",
						color=0xE3170A
					)
					embed.set_footer(text="sucks to be you")
					await context.send(embed=embed)
					self.autopic.reset_cooldown(context)

				else:
					for i in range(arg):
						pic = f'./assets/img/pic/{random.choice(os.listdir("./assets/img/pic"))}'
						await context.send(f"{i + 1}/{arg} images", file=discord.File(pic))
						if arg - i > 1:
							await asyncio.sleep(settings["autopicSleep"])

					if settings["autopicReturn"]:
						await context.send(f"*Cooldown has been set to **{settings['autopicCooldown']}s***")
			else:
				embed = discord.Embed(
					title="do you know how numbers work?",
					description="*use an integer*",
					color=0xE3170A
				)
				embed.set_footer(text="you is yesn't what")
				await context.send(embed=embed)
				self.autopic.reset_cooldown(context)
		else:
			embed = discord.Embed(
				title="party has been pooped by mods",
				description="*how dare they disable r!autopic*",
				color=0xE3170A
			)
			embed.set_footer(text="mods be ruining the fun innit")
			await context.send(embed=embed)
			self.autopic.reset_cooldown(context)

	@commands.command(name="succ", aliases=["succyea", "prayer"])
	@commands.cooldown(1, 2, BucketType.user)
	async def succ(self, context):
		await context.send(random.choice(succCommand))

	@commands.command(name="brit", aliases=["britbot", "britain", "bri'ish", "brits"])
	@commands.cooldown(1, 2, BucketType.user)
	async def brit(self, context):
		await context.send(random.choice(britCommand))

	@commands.command(name="uwu", aliases=["heresy", "cappybs", "bullshit", "bs"])
	@commands.cooldown(1, settings["uwuCooldown"], BucketType.guild)
	async def uwu(self, context):
		if context.channel.id in config["uwuChannel"] or settings["uwu"]:
			cum = random.choice([1, 0, 1, 0, 0, 1, 0])  # weighted random.choice
			if cum == 1:
				file = f'./assets/img/uwu/{random.choice(os.listdir("./assets/img/uwu"))}'
				await context.send(random.choice(["uwu", "UwU", "OwO", "ÒwÓ", "ÙwÚ", "ÓwÒ", "^w^", ":3"]), file=discord.File(file))

			else:
				await context.send(random.choice(uwuCommand))

			if settings["picReturn"]:
				await context.send(f"*To use this command outside <#884924639346823218> wait {settings['uwuCooldown']} seconds..*")

		else:
			embed = discord.Embed(
				title="Mods back at it again",
				description="Using this command outside <#884924639346823218> has been disabled.",
				color=0xE3170A
			)
			embed.set_footer(text="get mod'd, nerd")
			await context.send(embed=embed)

	@commands.command(name="reload", aliases=["restart"])
	@commands.has_role("devtools")
	async def reload(self, context):
		try:
			with open("assets/config.json") as file:
				global config
				config = json.load(file)

			with open("assets/settings.json") as file:
				global settings
				settings = json.load(file)
		except:
			embed = discord.Embed(title="An error occurred while reloading",
									description="your luck must be fucked",
									color=0xE3170A
									)
			await context.send(embed=embed)
		else:
			embed = discord.Embed(	title="Reload complete",	color=0x0C8708)
			await context.send(embed=embed)

	@commands.command(name="pain")
	@commands.cooldown(1, settings["painCooldown"], BucketType.guild)
	async def pain(self, context):
		pic = f'./assets/img/pain/{random.choice(os.listdir("./assets/img/pain"))}'
		msg = random.choice(["", "", "*pain.*", "*cri*", "not proud of that one", "very bigbrain moment", "so dumb smh",
								"mf"
								])
		await context.send(msg, file=discord.File(pic))

		if settings["painReturn"]:
			await context.send(f"*Cooldown has been set to **{settings['painCooldown']}s***")
		print(f"[r!pain], {pic}. {msg}\n")
		shortcut.logging(context.message, f"pic: {pic}, message: {msg}")

	@commands.command(name="test")
	async def test(self, context):
		await context.send("```python\nIndentationError: Unexpected indent [273, 3]\n```")
		await asyncio.sleep(3)
		await context.send("```python\n[Finished in 3.4s with exit code 1]\n```")


def setup(bot):
	bot.add_cog(General(bot))
