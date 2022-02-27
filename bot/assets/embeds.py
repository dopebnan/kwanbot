import discord


def unknown_error():
	embed = discord.Embed(
		title="UnknownError:",
		description="An unknown error has occured, try again or tell bnan",
		color=0xE3170A
	)
	embed.set_footer(text="sorry")

	return embed


def error_type():
	embed = discord.Embed(
		title="TypeError:",
		description=f"You used the wrong variable type",
		color=0xE3170A
	)
	embed.set_footer(text="dumbass")

	return embed


def error_invalid_arg(cmd):
	embed = discord.Embed(
		title="TypeError:",
		description=f"{cmd} got an invalid argument",
		color=0xE3170A
	)
	embed.set_footer(text="oof")

	return embed


def error_missing_role():
	embed = discord.Embed(
		title="MissingRoleError:",
		description="Your role isn't high enough to use Developer Commands and DevTools",
		color=0xE3170A
	)
	embed.set_footer(text="get fucked nerd")

	return embed


def author_not_in_vc():
	embed = discord.Embed(
		title="You're not in a vc",
		description="what are you, stupid?",
		color=0xE3170A
	)

	return embed


def bot_not_in_vc():
	embed = discord.Embed(
		title="I'm not even in vc",
		color=0xE3170A
	)

	return embed


def error_ytdl():
	embed = discord.Embed(
		title="That's not a video, dummy",
		description="It was probably a livestream or something",
		color=0xE3170A
	)

	return embed


def successful_save():
	embed = discord.Embed(
		title="Saving complete",
		description=f"Your changes have been applied.",
		color=0x0C8708
	)

	return embed


def added_to_queue(song):
	title = song['title']

	embed = discord.Embed(
		title=f"Added `{title}` to the queue",
		color=0x0C8708
	)

	return embed


def now_playing(context, song):
	title = song["title"]
	artist = song["artist"]

	embed = discord.Embed(
		title="Now playing",
		description=f"**{artist}** — *{title}*	[<@{context.id}>]",
		color=0xc96c0e
	)

	return embed
