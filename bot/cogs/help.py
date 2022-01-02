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

if not os.path.isfile("assets/version.json"):
	sys.exit("version.json not found.")
else:
	with open("assets/version.json") as f:
		version = json.load(f)


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
			value="get the bot latency"
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
			name="r!pain",
			value="Get a pic that invoked pain while making bot <:eww:894571137441357844>"
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

		gruvi_embed = discord.Embed(
			title="<:groovy:899682087114793050>GRUVI<:groovy:899682087114793050>",
			color=0x78a5fa
		)
		gruvi_embed.add_field(
			name="r!pop:",
			value="make bot pop into vc"
		)
		gruvi_embed.add_field(
			name="r!play *song*:",
			value="plays **song** (bruh-)"
		)
		gruvi_embed.add_field(
			name="r!playlocal *song*:",
			value="play a song from bot's directory"
		)
		gruvi_embed.add_field(
			name="r!songlist:",
			value="view songs in bot's directory"
		)
		gruvi_embed.add_field(
			name="r!cum:",
			value="queues the cum trilogy (locally)"
		)
		gruvi_embed.add_field(
			name="r!queue:",
			value="view the queue"
		)
		gruvi_embed.add_field(
			name="r!skip:",
			value="skip to the next song"
		)
		gruvi_embed.add_field(
			name="r!stop:",
			value="stop everything playing, and clear queue"
		)
		gruvi_embed.add_field(
			name="r!leave:",
			value="leave vc, no shit"
		)
		gruvi_embed.set_footer(text="GRUVI'S SPIRIT")

		await context.send(embed=embed)
		await context.send(embed=gruvi_embed)

	# DevTools
	@commands.command(name="devtools", aliases=["DevTools", "dt", "devhelp"])
	@commands.has_any_role(config["modID"][0], config["modID"][1])
	async def devtools(self, context):
		embed = discord.Embed(
			title="DevTools",
			description=f'{version["DEVTOOLVER"]}',
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
			value="*Reverts every settings to default (do a r!reload after it)*",
			inline=True
		)
		embed.add_field(
			name="r!picDev Cooldown __picCooldown: int__",
			value="*Change the cooldown for r!pic in seconds. Takes in an integer* ***(r!picDev Cooldown 30)***",
			inline=False
		)
		embed.add_field(
			name="r!picDev Return __picReturn: int__",
			value="*Turn the cooldown message on/off for r!pic* ***(r!picDev Return 0)***",
			inline=False
		)
		embed.add_field(
			name="r!autoDev Switch __autopic: int__",
			value="*Turn r!autopic on/off * ***(r!autoDev Switch 0)***",
			inline=False
		)
		embed.add_field(
			name="r!autoDev Sleep __autopicSleep: int__",
			value="*Change the cooldown inbetween images for r!autopic in seconds* ***(r!autoDev Sleep 15)***",
			inline=False
		)
		embed.add_field(
			name="r!autoDev Return __autopicReturn: int__",
			value="*Turn the cooldown message on/off for r!autopic* ***(r!autoDev Return 1)***",
			inline=False
		)
		embed.add_field(
			name="r!uwuDev Switch __uwu: bool__",
			value="*Turn r!uwu on/off* ***(r!uwuDev Switch 1)***",
			inline=False
		)
		embed.add_field(
			name="r!uwuDev Cooldown __uwuCooldown: int__",
			value="*Change the cooldown for r!uwu* ***(r!uwuDev Cooldown 15)***",
			inline=False
		)
		embed.add_field(
			name="r!uwuDev Return __uwuReturn: int__",
			value="*Turn the cooldown message on/off for r!uwu* ***(r!uwuDev Return 1)***",
			inline=False
		)
		embed.add_field(
			name="r!painDev Cooldown __painCooldown: int__",
			value="*Change the cooldown for r!pain* ***(r!painDev Cooldown 15)***",
			inline=False
		)
		embed.add_field(
			name="r!painDev Return __painReturn: int__",
			value="*Turn the cooldown message on/off for r!pain* ***(r!painDev Return 0)***",
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
