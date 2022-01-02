"""
Some stuff may have been yoinked from pawel02's image_bot. (dude literally saved this project)


imagine complying with legal stuff, couldn't be me smh
"""

# GRUVI'S SPIRIT

# TODO: playfile
import asyncio
import json
import os
import sys
import eyed3
from youtube_dl import YoutubeDL as ytdl

from assets import shortcut, embeds

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

popcat = "<a:popcat:888905645431070742>"


class Gruvi(commands.Cog, name="gruvi"):
	def __init__(self, bot):
		self.bot = bot

		self.is_playing = False

		self.music_queue = []
		self.q = []
		self.YDL_OPTS = {'format': 'bestaudio', "noplaylist": "true"}
		self.FFMPEG_OPTS = {'bopts': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', "opts": '-vn'}

		self.vc = ""
		self.ctx = ''

	def search_yt(self, item):
		with ytdl(self.YDL_OPTS) as ytdown:
			try:
				info = ytdown.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
			except Exception:
				return False

		return {'source': info['formats'][0]['url'],
				'title': info['title'],
				'artist': info['uploader'],
				'length': info['duration']
				}

	async def play_music(self):
		if len(self.music_queue) > 0:
			# i hate.
			self.is_playing = True
			self.vc = self.music_queue[0][1]
			song = self.music_queue[0][0]['source']
			auth = self.music_queue[0][2]

			embed = embeds.now_playing(auth, self.music_queue[0][0])
			await self.ctx.send(embed=embed)

			self.music_queue.pop(0)

			# mf really breaks without this, smh couldn't be me
			if not song.startswith("./"):
				a = self.FFMPEG_OPTS["bopts"]
				b = self.FFMPEG_OPTS["opts"]
			else:
				a = None
				b = None

			self.vc.play(discord.FFmpegPCMAudio(song, before_options=a, options=b),
							after=lambda e: asyncio.run_coroutine_threadsafe(self.play_music(), self.bot.loop))
		else:
			self.is_playing = False

	async def play_cum(self):
		if len(self.music_queue) > 0:
			# i hate.
			self.is_playing = True
			self.vc = self.music_queue[0][1]
			song = self.music_queue[0][0]['source']
			print(self.music_queue)
			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(song), after=lambda e:
							asyncio.run_coroutine_threadsafe(self.vc.guild.voice_client.disconnect(), self.bot.loop))

	@commands.command(name="pop", aliases=["j", "summon", "join"])
	async def pop(self, context):
		voice_client = context.guild.voice_client
		author_voice_client = context.author.voice

		if author_voice_client:
			vc = context.author.voice.channel

			if author_voice_client and not voice_client:
				await vc.connect()
				self.ctx = context
			elif author_voice_client:
				await voice_client.move_to(vc)

			embed = discord.Embed(
				title=f"{popcat}Popped in vc{popcat}",
				color=0x0C8708
			)
			await context.send(embed=embed)

		elif not author_voice_client:
			embed = discord.Embed(
				title="You need to be in a vc, dummy",
				color=0xE3170A
			)
			await context.send(embed=embed)

		elif context.bot.user in author_voice_client.channel.members:
			embed = discord.Embed(
				title="Already in vc, dummy",
				color=0x800085
			)
			await context.send(embed=embed)

	@commands.command(name="play", aliases=["p"])
	async def play(self, context, *args):
		voice_client = context.guild.voice_client
		vc = context.author.voice.channel

		arg = " ".join(args)

		if vc is None:
			await context.send(embed=embeds.author_not_in_vc())
		elif not voice_client:
			await context.send(embed=embeds.bot_not_in_vc())
		else:
			song = self.search_yt(arg)
			if isinstance(song, bool):
				await context.send(embed=embeds.error_ytdl())
			else:
				await context.send(embed=embeds.added_to_queue(song))
				self.music_queue.append([song, voice_client, context.author])
				self.q.append(song)

				if not self.is_playing:
					await self.play_music()

	@commands.command(name="playlocal", aliases=["pl"])
	async def playlocal(self, context, song):
		vc = context.author.voice.channel
		voice_client = context.guild.voice_client

		if vc is None:
			embed = embeds.author_not_in_vc()
			await context.send(embed=embed)

		elif not voice_client:
			embed = embeds.bot_not_in_vc()
			await context.send(embed=embed)

		else:
			if not os.path.isfile(f"./assets/audio/{song}.mp3"):
				raise discord.errors.InvalidArgument
			else:
				foo = shortcut.pseudo_ytdl_parse(song)
				self.music_queue.append([foo, voice_client, context.author])
				self.q.append(foo)
				await context.send(embed=embeds.added_to_queue(foo))

				if not self.is_playing:
					await self.play_music()

	@commands.command(name="songlist", aliases=["song", "music", "songs"])
	async def songlist(self, context, name=None):
		if name is None:
			song_list = os.listdir("./assets/audio/")
			x = ""

			for song in song_list:
				song_id = eyed3.load(f"./assets/audio/{song}")
				song = song.split('.', 1)[0]
				length = song_id.info.time_secs
				y = str(round(length % 60))
				if len(y) < 2:
					y = '0' + y
				length = str(round(length // 60)) + ':' + y
				x += f"{song}{' ' * (27 - len(song))}{length}\n"

			await context.send(f"```fsharp\nSonglist:\n{x}\n```")

	@commands.command(name="cum")
	async def cum(self, context):
		vc = context.author.voice.channel
		voice_client = context.guild.voice_client

		if vc is None:
			embed = embeds.author_not_in_vc()
			await context.send(embed=embed)
		elif not voice_client:
			embed = embeds.bot_not_in_vc()
			await context.send(embed=embed)
		else:
			for i in range(3):
				if i == 0:
					song = "cum_zone"
				elif i == 1:
					song = "cum_throne"
				elif i == 2:
					song = "last_cum"

				__song = shortcut.pseudo_ytdl_parse(song)
				self.music_queue.append([__song, voice_client, context.author])
				self.q.append(__song)

			await context.send("<:cum_zone:900770371698032640> WELCUM TO THE CUM ZONE <:cum_zone:900770371698032640>")

			if not self.is_playing:
				await self.play_music()

	@commands.command(name="queue", aliases=["q"])
	async def queue(self, context):
		print(self.q)
		result = shortcut.queue_format(self.q)
		print(result)

		if result != "":
			await context.send(result)
		else:
			await context.send("queue is empty")

	@commands.command(name="pause", aliases=["resume", "unpause"])
	async def pause(self, context):
		voice_client = context.guild.voice_client

		if not voice_client:
			embed = embeds.bot_not_in_vc()
			await context.send(embed=embed)
		else:
			if voice_client.is_playing():
				voice_client.pause()
				embed = discord.Embed(
					title="<:shut:894571138108231691> Paused <:shut:894571138108231691>",
					color=0x0C8708
				)
				await context.send(embed=embed)
			else:
				voice_client.resume()
				embed = discord.Embed(
					title="<:unshut:894571138645102643> Unpaused <:unshut:894571138645102643>",
					color=0x0C8708
				)
				await context.send(embed=embed)

	@commands.command(name="skip")
	async def skip(self, context):
		if self.vc != "":
			self.vc.stop()
			await context.send(embed=discord.Embed(title="Skipped song", color=0x0C8708))

	@commands.command(name="stop")
	async def stop(self, context):
		voice_client = context.guild.voice_client

		if not voice_client:
			embed = embeds.bot_not_in_vc()
			await context.send(embed=embed)

		else:
			if voice_client.is_playing():
				self.music_queue.clear()
				self.q.clear()
				voice_client.stop()
				embed = discord.Embed(title="Stopped the music", color=0x0C8708)
				await context.send(embed=embed)
			else:
				embed = discord.Embed(title="There's nothing to stop, dummy", color=0xE3170A)
				await context.send(embed=embed)

	@commands.command(name="leave", aliases=["die", "kys", "fuckyou", "disconnect", "d", "l"])
	async def leave(self, context):
		voice_client = context.guild.voice_client
		author_voice_client = context.author.voice

		if not author_voice_client:
			embed = embeds.author_not_in_vc()
			await context.send(embed=embed)

		elif not voice_client:
			embed = embeds.bot_not_in_vc()
			await context.send(embed=embed)

		elif context.bot.user in author_voice_client.channel.members:
			await context.guild.voice_client.disconnect()
			embed = discord.Embed(
				title="It's not like i wanted to join or anything! Dummy!",
				color=0x0C8708
			)
			await context.send(embed=embed)

			self.q.clear()


def setup(bot):
	bot.add_cog(Gruvi(bot))
