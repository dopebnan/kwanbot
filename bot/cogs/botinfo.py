"""
kwanCore, a discord.py bot foundation.
Copyright (C) 2022  dopebnan

kwanBot, images not included
Copyright (C) 2022 dopebnan

You should have received a copy of the GNU General Public License
along with kwanBot. If not, see <https://www.gnu.org/licenses/>.
"""

import os
from platform import platform, python_version

import discord
from discord.ext import commands

from shortcuts import terminal


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
            name="Core:",
            value="[kwanCore](https://github.com/dopebnan/kwancore) by [dopebnan](https://github.com/dopebnan)",
            inline=False
        )
        embed.add_field(
            name="kwanBot by:",
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
            description="You should open an [issue](https://github.com/dopebnan/kwanbot/issues) or ping <@696434931483803778>!",
            color=0x5de7b4
        )
        await ctx.send(embed=embed)

    @commands.command(name="sysinfo", aliases=["chkdsk", "filecheck", "fsck"], brief="Gives technical info about bot")
    async def sysinfo(self, ctx):
        pic_num = 0
        for ppl in os.listdir("usercontent/images/pic/"):
            pic_num += len(os.listdir("usercontent/images/pic/" + ppl))
        uwu_num = len(os.listdir("usercontent/images/uwu/"))
        pain_num = len(os.listdir("usercontent/images/pain/"))
        header = f"{self.bot.user.name}@[kwanCore]"
        latest_ver = terminal("git tag -l").split('\n')[-2]
        try:
            temp = terminal("vcgencmd measure_temp").split('=')[1].replace("'", '’')
        except IndexError:
            self.logger.log("warn", "stats", "Couldn't measure CPU temp, are you sure this is a raspberrypi?")
            temp = 0
        result = (f"```yaml\n"
                  f"{header}\n{'-' * len(header)}\n"
                  f"OS: {platform().split('-', 1)[0]}\n"
                  f"CPU: {temp}"
                  f"Uptime: {terminal(b'uptime -p').replace('up ', '')}"
                  f"Python: {python_version()}\n"
                  f"Discord.py: {discord.__version__}\n"
                  f"Current Version: {self.bot.version}\n"
                  f"Latest Version: {latest_ver}\n"
                  f"r!pic Images: {pic_num}\n"
                  f"r!uwu Images: {uwu_num}\n"
                  f"r!pain Images: {pain_num}\n"
                  f"```")
        await ctx.send(result)

    @commands.command(name="sourcecode", aliases=["gh", "source", "github"], brief="Checkout the inner workings of bot")
    async def sourcecode(self, ctx):
        embed = discord.Embed(
            title="Source code",
            description="You can view the source code on [GitHub](https://github.com/dopebnan/kwanbot)",
            color=discord.Color.random()
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(BotInfo(bot))
