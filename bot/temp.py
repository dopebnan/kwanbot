import discord
import json
import os.path
import sys

if not os.path.isfile("assets/config.json"):
    sys.exit("config.json not found.")
else:
    with open('assets/config.json') as f:
        config = json.load(f)

client = discord.Client()


@client.event
async def on_ready():
    print('Temporary bot.')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Migrating to discord.ext..."))
    print("yes")

@client.event
async def on_message(message):

    if message.content == "r!die" and message.author.id in config["modIDs"]:
        await client.change_presence(status=discord.Status.idle, activity=discord.Game("Migrating to discord.ext..."))
        print("yes")

    elif message.content.startswith("r!") or message.content.startswith("d!"):
        await message.channel.send("Bot is currently under maintenance, but will be back soon..")
    
client.run(config['TOKEN'])