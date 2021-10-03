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
		foo = {'source': f'./assets/audio/{song}.mp3', "title": bar.tag.title, "artist": bar.tag.artist}

		return foo
		
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

		class SuccessfulEmbeds:
			def SavingComplete(self):
				embed = discord.Embed(
					title="Saving complete",
					description=f"Your changes have been saved.",
					color=0x0C8708
					)
					
				embed.set_footer(text="you need to r!reload for your changes to take effect")

				return embed
