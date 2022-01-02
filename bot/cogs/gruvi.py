"""
Some stuff may have been yoinked from pawel02's image_bot. (dude literally saved this project)


imagine complying with legal stuff, couldn't be me smh
"""

# GRUVI'S SPIRIT

import json
import os
import sys
import eyed3
from youtube_dl import YoutubeDL as ytdl

from shortcut import Shortcut

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

		return {'source': info['formats'][0]['url'], 'title': info['title'], 'artist': info['uploader'], 'length': info['duration']}
	
	def play_next(self):
		if len(self.music_queue) > 0:
			self.is_playing = True

			song = self.music_queue[0][0]['source']
			auth = self.music_queue[0][2]

			self.music_queue.pop(0)

			if not song.startswith("./"):
				a = self.FFMPEG_OPTS["bopts"]
				b = self.FFMPEG_OPTS["opts"]
				print(True)
			else:
				a = None
				b = None

			self.vc.play(discord.FFmpegPCMAudio(song, before_options=a, options=b), after=lambda e: self.play_next())
		else:
			self.is_playing = False
	


	# function not used, probs needs deleting
	async def __play_music(self):
		if len(self.music_queue) > 0:
			self.is_playing = True

			url = self.music_queue[0][0]['source']

			'''if self.vc == "" or not self.vc.is_connected():
				self.vc = await self.music_queue[0][1].connect()
			else:
				self.vc = await self.bot.move_to(self.music_queue[0][1])'''

			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", options='-vn'), after=lambda e: self.play_next())
		else:
			self.is_playing = False
	
	async def local_play_music(self):
		if len(self.music_queue) > 0:
			# i hate.
			self.is_playing = True
			self.vc = self.music_queue[0][1]
			print(self.music_queue)
			song = self.music_queue[0][0]['source']	
			auth = self.music_queue[0][2]		
			print(song)

			embed = Shortcut.Embeds.Misc.nowPlaying(auth, self.music_queue[0][0])
			await self.ctx.send(embed=embed)
			
			self.music_queue.pop(0)

			# mf really breaks without this, smh couldn't be me
			if not song.startswith("./"):
				a = self.FFMPEG_OPTS["bopts"]
				b = self.FFMPEG_OPTS["opts"]
				print(True)
			else:
				a = None
				b = None

			self.vc.play(discord.FFmpegPCMAudio(song, before_options=a, options=b), after=lambda e: self.play_next())
	
	async def play_cum(self):
		if len(self.music_queue) > 0:
			# i hate.
			self.is_playing = True
			self.vc = self.music_queue[0][1]
			song = self.music_queue[0][0]['source']
			print(self.music_queue)
			self.music_queue.pop(0)

			self.vc.play(discord.FFmpegPCMAudio(song), after=lambda e: self.play_next)



	@commands.command(name="pop", aliases=["j", "summon", "join"])
	async def pop(self, context):
		voiceclient = context.guild.voice_client
		authvoice = context.author.voice

		if authvoice:
			vc = context.author.voice.channel

			if authvoice and not voiceclient:
				await vc.connect()
				self.ctx = context
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
	
	@commands.command(name="play", aliases=["p"])
	async def play(self, context, *args):
		voiceclient = context.guild.voice_client
		vc = context.author.voice.channel

		arg = " ".join(args)
		
		if vc is None:
			await context.send(embed=Shortcut.Embeds.Error.authorNotInVoice())
		elif not voiceclient:
			await context.send(embed=Shortcut.Embeds.Error.noBotVoice_client())
		else:
			song = self.search_yt(arg)
			if type(song) == type(True):
				await context.send(embed=Shortcut.Embeds.Error.ytdlErrorNotVideo())
			else:
				await context.send(embed=Shortcut.Embeds.Misc.addedToQueue(song))
				self.music_queue.append([song, voiceclient, context.author])
				self.q.append(song)

				if self.is_playing == False:
					await self.local_play_music()

	@commands.command(name="playlocal", aliases=["pl"])
	async def playlocal(self, context, song):
		vc = context.author.voice.channel
		voiceclient = context.guild.voice_client

		if vc is None:
			embed = Shortcut.Embeds.Error.authorNotInVoice()
			await context.send(embed=embed)

		elif not voiceclient:
				embed = Shortcut.Embeds.Error.noBotVoice_client()
				await context.send(embed=embed)

		else:
			if not os.path.isfile(f"./assets/audio/{song}.mp3"):
				raise discord.errors.InvalidArgument		
			else:
				foo = Shortcut.pseudo_ytdl_parse(song)
				self.music_queue.append([foo, voiceclient, context.author])
				self.q.append(foo)
				await context.send(embed=Shortcut.Embeds.Misc.addedToQueue(foo))
				
				if self.is_playing == False:
					await self.local_play_music()

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
				if len(y) < 2:
					y = '0' + y
				lenght = str(round( lenght // 60)) + ':' + y
				x += f"{song}{' ' * (27 - len(song))}{lenght}\n"

			await context.send(f"```fsharp\nSonglist:\n{x}\n```")

	@commands.command(name="cum")
	async def cum(self, context):
		vc = context.author.voice.channel
		voiceclient = context.guild.voice_client

		if vc is None:
			embed = Shortcut.Embeds.Error.authorNotInVoice()
			await context.send(embed=embed)
		elif not voiceclient:
				embed = Shortcut.Embeds.Error.noBotVoice_client()
				await context.send(embed=embed)
		else:
			for i in range(3):
				if i == 0:
					song = "cum_zone"
				elif i == 1:
					song = "cum_throne"
				elif i == 2:
					song = "last_cum"

				__song = Shortcut.pseudo_ytdl_parse(song)
				self.music_queue.append([__song, voiceclient, context.author])
				self.q.append(__song)

			await context.send("<:cum_zone:900770371698032640> WELCUM TO THE CUM ZONE <:cum_zone:900770371698032640>")

			if self.is_playing == False:
				await self.local_play_music()

	@commands.command(name="queue", aliases=["q"])
	async def queue(self, context):
		result = ""
		print(self.q)
		result = Shortcut.queueFormat(self.q)
		print(result)

		if result != "":
			await context.send(result)
		else:
			await context.send("queue is empty")
		
	@commands.command(name="pause", aliases=["resume", "unpause"])
	async def pause(self, context):
		voiceclient = context.guild.voice_client

		if not voiceclient:
			embed = Shortcut.Embeds.Error.noBotVoice_client()
			await context.send(embed=embed)
		else:
			if voiceclient.is_playing():
				voiceclient.pause()
				embed = discord.Embed(
					title="<:shut:894571138108231691> Paused <:shut:894571138108231691>",
					color=0x0C8708
				)
				await context.send(embed=embed)
			else:
				voiceclient.resume()
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
			self.play_next()

	@commands.command(name="stop")
	async def stop(self, context):
		voiceclient = context.guild.voice_client

		if not voiceclient:
			embed = Shortcut.Embeds.Error.noBotVoice_client()
			await context.send(embed=embed)
		
		else:
			if voiceclient.is_playing():
				self.music_queue.clear()
				self.q.clear()
				voiceclient.stop()
				embed = discord.Embed(title="Stopped the music", color=0x0C8708)
				await context.send(embed=embed)
			else:
				embed = discord.Embed(title="There's nothing to stop, dummy", color=0xE3170A)
				await context.send(embed=embed)

	@commands.command(name="leave", aliases=["die", "kys", "fuckyou", "disconnect", "d", "l"])
	async def leave(self, context):
		voiceclient = context.guild.voice_client
		authvoice = context.author.voice

		if not authvoice:
			embed = Shortcut.Embeds.Error.authorNotInVoice()
			await context.send(embed=embed)

		elif not voiceclient:
			embed = Shortcut.Embeds.Error.noBotVoice_client()
			await context.send(embed=embed)

		elif context.bot.user in authvoice.channel.members:
			await context.guild.voice_client.disconnect()
			embed = discord.Embed(
				title="It's not like i wanted to join or anything! Dummy!",
				color=0x0C8708
			)
			await context.send(embed=embed)

			self.q.clear()



def setup(bot):
	bot.add_cog(Gruvi(bot))
