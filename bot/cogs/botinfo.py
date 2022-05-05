"""
kwanCore, a discord.py bot foundation.
Copyright (C) 2022  dopebnan

kwanBot, images not included
Copyright (C) 2022 dopebnan

You should have received a copy of the GNU General Public License
along with kwanBot. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
from discord.ext import commands


class BotInfo(commands.Cog, name="Bot Info", description="Info about bot pogpog"):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger

    @commands.command(name="changelog", aliases=["changes", "updates"], brief="Sends the changelog, bruh")
    async def changelog(self, ctx):
        f = discord.File('../changelog.md')
        await ctx.send(file=f)

    @commands.command(name="info", brief="Sends the bot info")
    async def info(self, ctx):
        embed = discord.Embed(
            title="Info",
            description="Bot info pogpogpog",
            color=0x5de7b4
        )
        embed.add_field(
            name="kwanCore developer:",
            value="dopebnan",
            inline=False
        )
        embed.add_field(
            name="kwanBot developer:",
            value="dopebnan",
            inline=False
        )
        embed.add_field(
            name="Version:",
            value=f"{self.bot.version}",
            inline=True
        )
        await ctx.send(embed=embed)

    @commands.command(name="ping", brief="Checks the bot latency")
    async def ping(self, ctx):
        msg = f"The ping is {round(self.bot.latency * 1000)}ms"
        await ctx.send(msg)

    @commands.command(name="report", brief="Bot be buggy innit")
    async def report(self, ctx):
        embed = discord.Embed(
            title="Report",
            description="You should open an [issue](https://github.com/dopebnan/kwancore/issues)!",
            color=0x5de7b4
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BotInfo(bot))
