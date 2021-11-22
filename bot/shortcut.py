import time
import discord
import eyed3

class Shortcut:

	def getEmoji(context, discord, emojiname: str):
		return f'\{discord.utils.get(context.message.guild.emojis, name=emojiname)}'

	def variables(self, var: str):
		author = var.author
		ID = author.id

		return author, ID

	def varType(arg: str):
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

	def logging(message, errormsg=None, skip=False):
			with open("./logs/log.txt", 'a') as f:
				if skip is True:
					f.write(f"[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}] <{message.author}, ({message.author.id})>: {errormsg}\n")
				else:
					f.write(f"[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}] <{message.author}, ({message.author.id})>: {errormsg} ({message.content})\n")

	def pseudo_ytdl_parse(song):
		bar = eyed3.load(f"./assets/audio/{song}.mp3")
		
		lenght = round(int(bar.info.time_secs))

		foo = {'source': f'./assets/audio/{song}.mp3', "title": bar.tag.title, "artist": bar.tag.artist, "length": lenght}

		return foo
	
	def queueFormat(queue):
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
		class Error:
			def GenericError():
				embed = discord.Embed(
					title="UnknownError:",
					description="An unknown error has occured, try again or tell bnan",
					color=0xE3170A
				)
				embed.set_footer(text="sorry")

				return embed
			
			def TypeErrorEmbed():
				embed = discord.Embed(
					title="TypeError:",
					description=f"You used the wrong variable type",
					color=0xE3170A
				)
				embed.set_footer(text="dumbass")

				return embed

			def InvalidArgumentError(cmd):
				embed = discord.Embed(
					title="TypeError:",
					description=f"{cmd} got an invalid argument",
					color=0xE3170A
				)
				embed.set_footer(text="oof")

				return embed
		
			def MissingRoleError():
				embed = discord.Embed(
					title="MissingRoleError:",
					description="Your role isn't high enough to use Developer Commands and DevTools",
					color=0xE3170A
				)
				embed.set_footer(text="get fucked nerd")

				return embed
			
			def authorNotInVoice():
				embed = discord.Embed(
					title="You're not in a vc",
					description="what are you, stupid?",
					color=0xE3170A
				)
				return embed

			def noBotVoice_client():
				embed = discord.Embed(
					title="I'm not even in vc",
					color=0xE3170A
				)
				return embed

			def ytdlErrorNotVideo():
				embed = discord.Embed(
					title="That's not a video, dummy",
					description="It was probably a livestream or something",
					color=0xE3170A
				)
				return embed

		class Misc:
			def SavingComplete():
				embed = discord.Embed(
					title="Saving complete",
					description=f"Your changes have been saved.",
					color=0x0C8708
					)
					
				embed.set_footer(text="you need to r!reload for your changes to take effect")

				return embed
			
			def addedToQueue(song):
				title = song['title'] 
				
				embed = discord.Embed(
					title=f"Added `{title}` to the queue",
					color=0x0C8708					
				)
				
				return embed
			
			def nowPlaying(context, song):
				title = song["title"]
				artist = song["artist"]
				
				embed = discord.Embed(
					title="Now playing",
					description=f"**{artist}** — *{title}*	[<@{context.id}>]",
					color=0xc96c0e
				)
				
				return embed
				