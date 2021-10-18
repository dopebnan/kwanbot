import time
import discord
import eyed3

class Shortcut:

	def getEmoji(self, context, discord, emojiname: str):
		return f'\{discord.utils.get(context.message.guild.emojis, name=emojiname)}'

	def variables(self, var: str):
		author = var.author
		ID = author.id

		return author, ID

	def fileType(self, arg: str):
		if arg == 'True' or arg == 'False':
			ftype = 'bool'
		elif arg == None:
			ftype = "None"
		elif arg.isnumeric():
			ftype = 'int'
		elif arg.split('.', 1)[0].isnumeric():
			ftype = 'float'
		else:
			ftype = 'str'
	
		return ftype

	def logging(self, message, errormsg=None):
		with open("./logs/log.txt", 'a') as f:
			f.write(f"[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}] <{message.author}, ({message.author.id})>: {errormsg} ({message.content})\n")

	def pseudo_ytdl_parse(self, song):
		bar = eyed3.load(f"./assets/audio/{song}.mp3")
		
		lenght = round(int(bar.info.time_secs))
		'''y = str(round(lenght % 60))
		if len(y) < 2:
			y = '0' + y
		lenght = str(round( lenght // 60)) + ':' + y'''

		foo = {'source': f'./assets/audio/{song}.mp3', "title": bar.tag.title, "artist": bar.tag.artist, "length": lenght}

		return foo
	
	def queueFormat(self, queue):
		result = f"```fsharp\n"
		for i in range(0, len(queue)):
			foo = queue[i]['title'] + ' — ' + queue[i]['artist']
			length = queue[i]['length']
			y = str(round(length % 60))
			if len(y) < 2:
				y = '0' + y
			length = str(round(length // 60)) + ':' + y

			if len(foo) > 36:
				foo = [foo[x:x+36] for x in range(0, len(foo), 36)][0]
				foo += "…"
			else:
				foo = foo + ' ' * (37 - len(foo))
			
			result += f" {i}) {foo} {length}      \n"
		
		result += "\n    Das the end of the queue!\n```"

		return result
			
		
	class Embeds:
		def GenericError(self):
			embed = discord.Embed(
				title="UnknownError:",
				description="An unknown error has occured, try again or tell bnan",
				color=0xE3170A
			)
			embed.set_footer(text="sorry")

			return embed
	
		def TypeErrorEmbed(self, type1: str, ftype: str):
			embed = discord.Embed(
				title="TypeError:",
				description=f"a {type1} is required (got {ftype})",
				color=0xE3170A
			)
			embed.set_footer(text="dumbass")

			return embed

		def InvalidArgumentError(self, cmd):
			embed = discord.Embed(
				title="TypeError:",
				description=f"{cmd} got an invalid argument",
				color=0xE3170A
			)
			embed.set_footer(text="oof")

			return embed
		
		def MissingRoleError(self):
			embed = discord.Embed(
				title="MissingRoleError:",
				description="Your role isn't high enough to use Developer Commands and DevTools",
				color=0xE3170A
			)
			embed.set_footer(text="get fucked nerd")

			return embed
		
		class BotEmbeds:
			def authorNotInVoice(self):
				embed = discord.Embed(
					title="You're not in a vc",
					description="what are you, stupid?",
					color=0xE3170A
				)
				return embed
			def noBotVoice_client(self):
				embed = discord.Embed(
					title="I'm not even in vc",
					color=0xE3170A
				)
				return embed
			
			def ytdlErrorNotVideo(self):
				embed = discord.Embed(
					title="That's not a video, dummy",
					description="It was probably a livestream or something",
					color=0xE3170A
				)
				return embed

		class SuccessfulEmbeds:
			def SavingComplete(self):
				embed = discord.Embed(
					title="Saving complete",
					description=f"Your changes have been saved.",
					color=0x0C8708
					)
					
				embed.set_footer(text="you need to r!reload for your changes to take effect")

				return embed
			
			def addedToQueue(self, song):
				title = song['title'] 
				
				embed = discord.Embed(
					title=f"Added `{title}` to the queue",
					color=0x0C8708					
				)
				
				return embed
			
			# if i dont make this typo, it wont work
			def nowPalying(self, context, song):
				title = song["title"]
				artist = song["artist"]
				
				embed = discord.Embed(
					title="Now playing",
					description=f"**{artist}** — *{title}*	[<@{context.author.id}>]",
					color=0xc96c0e
				)
				
				return embed
				