"""
kwanCore, a discord.py bot foundation.
Copyright (C) 2022  dopebnan

kwanBot, images not included
Copyright (C) 2022 dopebnan

You should have received a copy of the GNU General Public License
along with kwanBot. If not, see <https://www.gnu.org/licenses/>.
"""

import urbandictionary as urbdic
import asyncpraw

import discord
from discord.ext import commands


class Memes(commands.Cog, name="Memes", description="Newer fun stufff"):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger
        self.reddit = asyncpraw.Reddit(
            client_id=bot.config["reddit"]['client_id'],
            client_secret=bot.config["reddit"]['client_secret'],
            password=bot.config["reddit"]['password'],
            user_agent=bot.config["reddit"]['user_agent'],
            username=bot.config["reddit"]['username']
        )
        self.upvote = bot.config["emojis"]["upvote"]
        self.downvote = bot.config["emojis"]["downvote"]

    async def get_post_embed(self, subreddit, color=None, timeout=10):
        """
        Get a random image from a subreddit

        :param subreddit:  str, the subreddit name
        :param color:  int, the embed color
            Default: None
        :param timeout:  int, the amount of loops it should do before stopping;
            Default:  10
        """
        subreddit = await self.reddit.subreddit(subreddit)
        submission = await subreddit.random()
        i = 0

        while not submission.post_hint == "image":
            if i >= timeout:
                raise TimeoutError("Couldn't find an image")
            # if 10 posts didn't have an image, then that's worrying
            i += 1
            submission = await subreddit.random()

        self.logger.log("info", "get_post_embed", f"Found {submission.permalink} from {submission.subreddit}")
        embed = discord.Embed(
            title=submission.title,
            url=submission.url,
            color=color
        )
        embed.set_image(url=submission.url)
        embed.set_footer(text=f"Posted by u/{submission.author} in r/{submission.subreddit}")
        return embed

    @commands.command(name="memes", brief="Gets you some of the freshest memes")
    async def memes(self, ctx):
        embed = await self.get_post_embed("memes+dankmemes", 0x29024a)
        await ctx.send(embed=embed)

    @commands.command(name="tifu", brief="See people fuck up badly")
    async def tifu(self, ctx):
        async with ctx.typing():
            subreddit = await self.reddit.subreddit("tifu")
            submission = await subreddit.random()
            while not submission.link_flair_text == "S":
                submission = await subreddit.random()
            embed = discord.Embed(
                title=submission.title,
                url=submission.url,
                description=submission.selftext,
                color=0x316ebb
            )
            embed.set_footer(text=f"Posted by u/{submission.author} in r/{submission.subreddit}")
            await ctx.send(embed=embed)

    @commands.command(name="wholesome", brief="The wholesome side of the internet")
    async def wholesome(self, ctx):
        embed = await self.get_post_embed("wholesomememes+comfypasta", 0xf4a261)
        await ctx.send(embed=embed)

    @commands.command(name="shitpost", aliases=["shitposts", "shitposting"], brief="Poopy stinky posts")
    async def shitpost(self, ctx):
        embed = await self.get_post_embed("shitposting+skamtebord+196+surrealmemes", 0x885144)
        await ctx.send(embed=embed)

    @commands.command(name="meirl", aliases=["me_irl"], brief="Selfies of the soul")
    async def meirl(self, ctx):
        embed = await self.get_post_embed("me_irl+discord_irl+me_irlgbt", 0x510000)
        await ctx.send(embed=embed)

    @commands.command(name="tumblr", brief="Internet’s favourite hellsite")
    async def tumblr(self, ctx):
        embed = await self.get_post_embed("tumblr", 0x6b788c)
        await ctx.send(embed=embed)

    @commands.command(name="urban", aliases=["urbdic", "urban_dictionary"],
                      brief="Get a definition from the holy Urban Dictionary")
    async def urban(self, ctx, *term):
        term = ' '.join(term)
        defs = urbdic.define(term)
        try:
            embed = discord.Embed(
                title=defs[0].word.title(),
                description=defs[0].definition.replace('[', '__**').replace(']', '**__'),
                color=0x00ff64
            )
            embed.add_field(name='\u200b', value=f"*{defs[0].example.replace('[', '__**').replace(']', '**__')}*")
            embed.add_field(name=f"{self.upvote} **{defs[0].upvotes - defs[0].downvotes}** {self.downvote}",
                            value='\u200b', inline=False)
            self.logger.log("info", "urban", f"Found {defs[0].word}")
        except IndexError:
            embed = discord.Embed(
                title=r"¯\_(ツ)_/¯",
                description=f"**Sorry, we couldn't find: *{term}***",
                color=0xff0032
            )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Memes(bot))
