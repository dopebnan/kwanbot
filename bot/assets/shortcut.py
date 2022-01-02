import time
import discord
import eyed3

def get_emoji(context, _discord, emoji_name: str):
	return f'\\{discord.utils.get(context.message.guild.emojis, name=emoji_name)}'


def var_type(arg: str):
	if arg == 'True' or arg == 'False':
		filetype = 'bool'
	elif arg is None:
		filetype = "None"
	elif arg.isnumeric():
		filetype = 'int'
	elif arg.split('.', 1)[0].isnumeric():
		filetype = 'float'
	else:
		filetype = 'str'

	return filetype


def logging(message, error_msg=None, skip=False):
	with open("./logs/log.txt", 'a') as f:
		if skip is True:
			f.write(f"[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}] "
					f"<{message.author}, ({message.author.id})>: {error_msg}\n")
		else:
			f.write(f"[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}] "
					f"<{message.author}, ({message.author.id})>: {error_msg} ({message.content})\n")


def pseudo_ytdl_parse(song):
	song_obj = eyed3.load(f"./assets/audio/{song}.mp3")
	length = round(int(song_obj.info.time_secs))
	song_atr = {'source': f'./assets/audio/{song}.mp3',
				"title": song_obj.tag.title,
				"artist": song_obj.tag.artist,
				"length": length
				}

	return song_atr


def queue_format(queue):
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
