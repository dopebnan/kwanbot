import random
import discord
import json
import os.path
import sys

from discord.ext import tasks
from discord.ext.commands.bot import Bot

if not os.path.isfile("assets/config.json"):
	sys.exit("config.json not found.")
else:
	with open('assets/config.json') as f:
		config = json.load(f)

statuses = ["Currently getting updated", "Under maintenance", "r!help", "Going on a pee break",
			"Taking a fat nasty shit", "Absolutely ripping ass"]

bot = Bot(command_prefix="r!")


@bot.event
async def on_ready():
	print(f'        Kwanbot!\n    bot: {bot.user.name}\n\n\n')
	status_task.start()
	

@tasks.loop(minutes=6.0)
async def status_task():
	await bot.change_presence(activity=discord.Game(random.choice(statuses)), status=discord.Status.idle, afk=True)
	print("Changed status")

bot.remove_command("help")


@bot.event
async def on_message(message):
	if message.content.startswith("r!"):
		embed = discord.Embed(
			title="Bot down",
			description="Currently getting updated innit",
			color=0xB000B5
		)
		await message.channel.send(embed=embed)
	
	await bot.process_commands(message)


bot.run(config['TOKEN'])
