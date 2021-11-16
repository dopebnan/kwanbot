"""
Moved it here to make it easier to modify/make the other code easier to read
"""

import json
import os
import sys

import discord
from discord.ext import commands

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



class Help(commands.Cog, name="help"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name='help')
	async def help(self, context):
		embed = discord.Embed(
			title="commands ayyy",
			color=0x7209B7
		)
		embed.add_field(
			name="r!changelog:",
			value="see the changelog, bruh"
		)
		embed.add_field(
			name="r!bugtracker:",
			value="see the bugs"
		)
		embed.add_field(
			name="r!check:",
			value="like r!info, but more technical stuff"
		)
		embed.add_field(
			name="r!sourcecode",
			value="view the repo of the bot"
		)
		embed.add_field(
			name="r!help:",
			value="this."
		)
		embed.add_field(
			name="r!info:",
			value="info about bot <:pogfield:884844071733055488><:pogfield:884844071733055488>"
		)
		embed.add_field(
			name="r!ping:",
			value="get the bot ping"
		)
		embed.add_field(
			name="r!report:",
			value="bot be buggy innit",
			inline=False
		)
		embed.add_field(
			name="r!pic:",
			value="out of context pics",
			inline=True
		)
		embed.add_field(
		   name="r!autopic x:",
		   value="Loops r!pic for **x** amount of times",
		   inline=True
		)
		embed.add_field(
			name="r!succ:",
			value="ZE HOLI BUSSY PRAYERZ SUCCSUCCSUCC <:jus:884844071766622258>",
			inline=False
		)
		embed.add_field(
			name="r!brit:",
			value=":flag_gb: :eyes:",
			inline=True
		)
		embed.add_field(
			name="r!uwu:",
			value="cappy bullshit",
			inline=True
		)
		embed.set_footer(text=f"mh yez, very")

		membed = discord.Embed(
			title="<:groovy:899682087114793050>GRUVI<:groovy:899682087114793050>",
			color=0x78a5fa
		)
		membed.add_field(
			name="r!pop:",
			value="make bot pop into vc"
		)
		membed.add_field(
			name="r!play *song*:",
			value="plays **song** (bruh-)"
		)
		membed.add_field(
			name="r!playlocal *song*:",
			value="play a song from bot's directory"
		)
		membed.add_field(
			name="r!songlist:",
			value="view songs in bot's directory"
		)
		membed.add_field(
			name="r!cum:",
			value="queues the cum trilogy (locally)"
		)
		membed.add_field(
			name="r!queue:",
			value="view the queue"
		)
		membed.add_field(
			name="r!skip:",
			value="skip to the next song"
		)
		membed.add_field(
			name="r!stop:",
			value="stop everything playing, and clear queue"
		)
		membed.add_field(
			name="r!leave:",
			value="leave vc, no shit"
		)
		membed.set_footer(text="GRUVI'S SPIRIT")

		await context.send(embed=embed)
		await context.send(embed=membed)



	@commands.command(name="devtools", aliases=["DevTools", "dt", "devhelp"])
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def devtools(self, context):
		embed = discord.Embed(
			title="DevTools",
			description=f'{config["DEVTOOLVER"]}',
			color=0x6F2377
		)
		embed.add_field(
			name="r!filecheck:",
			value="*Gives technical info about bot*",
			inline=True
		)
		embed.add_field(
			name="r!debug:",
			value="*Changes settings.json into dev-mode*",
			inline=True
		)
		embed.add_field(
			name="r!reset",
			value="*Reverts every setting to default (do a r!reload after it)*",
			inline=True
		)
		embed.add_field(
			name="r!picDev Cooldown __picCooldown: int__",
			value="*Change the cooldown for r!pic in seconds. Takes in an integer* ***(r!picCooldown 30)***",
			inline=False
		)
		embed.add_field(
			name="r!picDev Return __picReturn: bool__",
			value="*Turn on/off the cooldown message for r!pic* ***(r!picReturn False)***",
			inline=False
		)
		embed.add_field(
			name="r!autoDev Switch __autopic: bool__",
			value="*Turn on/off r!autopic* ***(r!autoSwitch False)***",
			inline=False
		)
		embed.add_field(
			name="r!autoDev Sleep __autopicSleep: int__",
			value="*Change the cooldown inbetween images for r!autopic in seconds* ***(r!autoSwitch False)***",
			inline=False
		)
		embed.add_field(
			name="r!autoDev Return __autopicReturn: bool__",
			value="*Turn on/off the cooldown message for r!autopic* ***(r!autoReturn True)***",
			inline=False
		)
		embed.add_field(
			name="r!uwuDev Switch __uwu: bool__",
			value="*Turn on/off r!uwu* ***(r!uwuSwitch True)***",
			inline=False
		)
		embed.add_field(
			name="r!uwuDev Cooldown __uwuCooldown: int__",
			value="*Turn on/off r!uwu* ***(r!uwuSwitch True)***",
			inline=False
		)
		embed.add_field(
			name="r!log __*args: str__",
			value="*If no arguments given, gives you the log file. Otherwise logs the arguments*",
			inline=True
		)
		embed.add_field(
			name="r!newlog",
			value="*Creates a new log.txt*"
		)
		await context.send(embed=embed)



def setup(bot):
	bot.add_cog(Help(bot))