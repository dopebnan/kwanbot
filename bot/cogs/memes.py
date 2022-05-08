"""
kwanCore, a discord.py bot foundation.
Copyright (C) 2022  dopebnan

You should have received a copy of the GNU General Public License
along with kwanCore. If not, see <https://www.gnu.org/licenses/>.
"""

import aiohttp
import asyncpraw

import discord
from discord.ext import commands


async def is_pic(url):
    async with aiohttp.ClientSession() as session:
        async with session.head(url) as r:
            return str(r.headers.get("Content-Type")).startswith("image/")


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

    async def get_post_embed(self, subreddit, embed_name, timeout=10):
        """
        Get a random image from a subreddit

        :param subreddit:  str, the subreddit name
        :param embed_name:  str, the title of the embed
        :param timeout:  int, the amount of loops it should do before stopping;
            Default:  10
        """
        subreddit = await self.reddit.subreddit(subreddit)
        submission = await subreddit.random()
        i = 0
        while not await is_pic(submission.url):
            if i >= timeout:
                raise TimeoutError("Couldn't find an image")
            # if 10 posts didn't have an image, then that's worrying
            i += 1
            submission = await subreddit.random()

        embed = discord.Embed(
            title=embed_name,
            color=discord.Color.random()
        )
        embed.set_image(url=submission.url)
        embed.set_footer(text=f"Posted by u/{submission.author} in r/{submission.subreddit}")
        return embed

    @commands.command(name="memes", brief="Gets you some of the freshest memes")
    async def memes(self, ctx):
        embed = await self.get_post_embed("memes+dankmemes", "Memes")
        await ctx.send(embed=embed)

    @commands.command(name="tifu", brief="See people fucking up badly")
    async def tifu(self, ctx):
        subreddit = await self.reddit.subreddit("tifu")
        submission = await subreddit.random()
        while not submission.link_flair_text == "S":
            submission = await subreddit.random()
        embed = discord.Embed(
            title=submission.title,
            url=submission.url,
            description=submission.selftext
        )
        embed.set_footer(text=f"Posted by u/{submission.author} in r/{submission.subreddit}")
        await ctx.send(embed=embed)









def setup(bot):
    bot.add_cog(Memes(bot))
