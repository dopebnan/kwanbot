"""
Some stuff may have been yoinked from pawel02's image_bot.


imagine complying with legal stuff, couldn't be me smh
"""

# GRUVI'S SPIRIT

import json
import os
import sys
import random
import asyncio
import eyed3
from youtube_dl import YoutubeDL as ytdl

from shortcut import Shortcut

import discord
from discord.ext import commands
from discord.ext.commands import BucketType


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






class Gruvi(commands.Cog, name="gruvi"):
	def __init__(self, bot):
		self.bot = bot

		self.is_playing = False

		self.music_queue = []
		self.YDL_OPTS = {'format': 'bestaudio', "noplaylist": "true"}
		self.FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', "options": '-vn'}

		self.vc = ""

	def search_yt(self, item):
		with ytdl(self.YDL_OPTS) as ytdown:
			try:
				info = ytdown.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
			except Exception:
				return False
			
		return {'source': info['formats'][0]['url'], 'title': info['title'], 'artist': info['uploader']}
	

	def play_next(self):
		if len(self.music_queue) > 0:
			self.is_playing = True

			url = self.music_queue[0][0]['source']

			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(url), after=lambda e: self.play_next())

		else:
			self.is_playing = False

	async def __play_music(self):
		if len(self.music_queue) > 0:
			self.is_playing = True

			url = self.music_queue[0][0]['source']

			'''if self.vc == "" or not self.vc.is_connected():
				self.vc = await self.music_queue[0][1].connect()
			else:
				self.vc = await self.bot.move_to(self.music_queue[0][1])'''

			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(url), after=lambda e: self.play_next())
		else:
			self.is_playing = False
	
	async def local_play_music(self):
		if len(self.music_queue) > 0:
			# i hate.
			self.is_playing = True
			
			self.vc = self.music_queue[0][1]

			print(self.music_queue)

			song = self.music_queue[0][0]['source']
			self.music_queue.pop(0)

			print(song)

			self.vc.play(discord.FFmpegPCMAudio(song), after=lambda e: self.play_next())

	@commands.command(name="pop", aliases=["j", "summon", "join"])
	async def pop(self, context):
		voiceclient = context.guild.voice_client
		authvoice = context.author.voice

		if authvoice:
			vc = context.author.voice.channel
			if authvoice and not voiceclient:
				await vc.connect()
			
			elif authvoice:
				await voiceclient.move_to(vc)

			embed = discord.Embed(
				title="<a:popcat:888905645431070742>Popped in vc<a:popcat:888905645431070742>",
				color=0x0C8708
				)
			await context.send(embed=embed)
		
		elif not authvoice:
			embed = discord.Embed(
			title="You need to be in a vc, dummy",
			color=0xE3170A
			)

			await context.send(embed=embed)
		
		elif context.bot.user in authvoice.channel.members:
			embed = discord.Embed(
				title="Already in vc, dummy",
				color=0x800085
			)
			
			await context.send(embed=embed)
	
	@commands.command(name="leave", aliases=["die", "kys", "fuckyou", "disconnect", "d"])
	async def leave(self, context):
		voiceclient = context.guild.voice_client
		authvoice = context.author.voice

		if not voiceclient:
			embed = discord.Embed(
				title="You're not in a vc",
				description="what are you, stupid?",
				color=0xE3170A
			)

			await context.send(embed=embed)

		elif context.bot.user in authvoice.channel.members:
			await context.guild.voice_client.disconnect()
			embed = discord.Embed(
				title="It's not like i wanted to join or anything! Dummy!",
				color=0x0C8708
			)
			
			await context.send(embed=embed)
		
	@commands.command(name="playlocal", aliases=["pl"])
	async def playlocal(self, context, song):
		vc = context.author.voice.channel
		voiceclient = context.guild.voice_client

		if vc is None:
			await context.send("VoiceError: author not connected to voice.channel")

		if not voiceclient:
				await context.send("VoiceError: bot voice client doesn't exist")

		else:
			if not os.path.isfile(f"./assets/audio/{song}.mp3"):
				raise commands.BadArgument
			
			else:
				await context.send("added to queeueuueueueu")
				foo = Shortcut().pseudo_ytdl_parse(song)
				self.music_queue.append([foo, voiceclient])

				if self.is_playing == False:
					await self.local_play_music()
				
				'''embed = discord.Embed(
					title="Now playing",
					description=f"**{songf.tag.artist}** — *{songf.tag.title}*    [<@{context.author.id}>]",
					color=0xf49411
				)
				await context.send(embed=embed)'''

	@commands.command(name="play", aliases=["p"])
	async def play(self, context, *args):
		voiceclient = context.guild.voice_client
		vc = context.author.voice.channel

		arg = " ".join(args)
		
		if vc is None:
			await context.send("VoiceError: author not connected to voice.channel")
		elif not voiceclient:
			await context.send("VoiceError: bot voice client doesn't exist")
		else:
			song = self.search_yt(arg)
			if type(song) == type(True):
				await context.send("Youtube_dlError: ArgumentError: Argument is a livestream")
			else:
				await context.send("added to qwuuqueuweueuue")
				self.music_queue.append([song, voiceclient])

				if self.is_playing == False:
					await self.local_play_music()

	@commands.command(name="pause", aliases=["resume", "unpause"])
	async def pause(self, context):
		voiceclient = context.guild.voice_client

		if not voiceclient:
			embed = discord.Embed(
			title="You need to be in a vc, dummy",
			color=0xE3170A
			)

			await context.send(embed=embed)
		
		
		else:
			if voiceclient.is_playing():
				voiceclient.pause()
				embed = discord.Embed(
					title="Paused",
					color=0x0C8708
				)
				await context.send(embed=embed)

			else:
				voiceclient.resume()
				embed = discord.Embed(
					title="Resumed",
					color=0x0C8708
				)
				await context.send(embed=embed)

	@commands.command(name="stop")
	async def stop(self, context):
		voiceclient = context.guild.voice_client

		if not voiceclient:
			embed = discord.Embed(
			title="You need to be in a vc, dummy",
			color=0xE3170A
			)
			await context.send(embed=embed)
		
		else:
			if voiceclient.is_playing():
				voiceclient.stop()
				embed = discord.Embed(title="Stopped", color=0x0C8708)
				await context.send(embed=embed)
			else:
				embed = discord.Embed(title="There's nothing to stop, dummy", color=0xE3170A)
				await context.send(embed=embed)

	@commands.command(name="songlist", aliases=["song", "music", "songs"])
	async def songlist(self, context, name=None):
		if name == None:
			songlist = os.listdir("./assets/audio/")
			x = ""
			for song in songlist:
				SONGID = eyed3.load(f"./assets/audio/{song}")
				song = song.split('.', 1)[0]
				lenght = SONGID.info.time_secs
				y = str(round(lenght % 60))
				lenght = str(round( lenght // 60)) + ':' + y
				x += f"{song}{' ' * (27 - len(song))}{lenght}\n"
				
			await context.send(f"```fsharp\nSonglist:\n{x}\n```")

	@commands.command(name="queue", aliases=["q"])
	async def queue(self, context):
		result = ""
		for i in range(0, len(self.music_queue)):
			result += self.music_queue[i][0]['title'] + "\n"

		print(result)
		if result != "":
			await context.send(result)
		else:
			await context.send("no music in queueuueueue")
		
	@commands.command(name="skip")
	async def skip(self, context):
		if self.vc != "":
			self.vc.stop()
			await self.local_play_music()
			

	async def on_command_error(context, error):

		if isinstance(error, discord.ClientException):
			if context.command.qualified_name == "play" or context.command.qualified_name == "playlocal":
				print('asd')

def setup(bot):
	bot.add_cog(Gruvi(bot))
