"""
kwanCore, a discord.py bot foundation.
Copyright (C) 2022  dopebnan

kwanBot, images not included
Copyright (C) 2022 dopebnan

You should have received a copy of the GNU General Public License
along with kwanCore. If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
import json
import os
import random

import discord
from discord.ext import commands
from discord.ext.commands import BucketType

with open("usercontent/settings.json") as file:
    settings = json.load(file)


class BotInfo(commands.Cog, name="Bot Info", description="Stuff about the bot"):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger
        self.replies = bot.config["general"]

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

    @commands.command(name="pic", brief="Out of context pictures innit")
    @commands.cooldown(1, settings["pic_cooldown"], BucketType.user)
    async def pic(self, ctx):
        p = "usercontent/images/pic/"
        img = p + random.choice(os.listdir(p))
        msg = random.choice(["remember this:", "bruh", "pic pog", ":kwanbruh:"])
        await ctx.send(msg, file=discord.File(img))
        self.logger.log("info", "pic", f"Sent {img} to #{ctx.channel}")

    @commands.command(name="autopic", aliases=["pix", "pics"], brief="MORE OUT OF CONTEXT PICS")
    @commands.cooldown(1, settings["autopic_sleep"]*6, BucketType.user)
    async def autopic(self, ctx, i=None):
        try:
            i = int(i)
        except ValueError:
            self.autopic.reset_cooldown(ctx)
            raise TypeError("Do you know how numbers work??")
        if i > 10:
            self.autopic.reset_cooldown(ctx)
            raise TypeError("I can't go over 10 (pick a smaller number)")
        if i > 0:
            for j in range(i):
                p = "usercontent/images/pic/"
                img = p + random.choice(os.listdir(p))
                msg = random.choice(["remember this:", "bruh", "pic pog", ":kwanbruh:"]) + f" ({j + 1}/{i})"
                await ctx.send(msg, file=discord.File(img))
                self.logger.log("info", "autopic", f"Sent {img} to #{ctx.channel} ({j + 1}/{i})")
                await asyncio.sleep(settings["autopic_sleep"])

    @commands.command(name="succ", brief="HOLI BUSSY PRAYERZ SUCCSUCCSUCC")
    async def succ(self, ctx):
        await ctx.send(random.choice(self.replies["succ"]))

    @commands.command(name="brit", brief="God save the Queen")
    async def brit(self, ctx):
        await ctx.send(random.choice(self.replies["brit"]))

    @commands.command(name="uwu", aliases=["heresy", "cappybs"], brief="Only the Finest Cappy Bullshit:tm: 24/7")
    @commands.cooldown(1, settings["uwu_cooldown"], BucketType.user)
    async def uwu(self, ctx):
        if ctx.channel.id != self.bot.config["uwu_channel"] and not settings["uwu"]:
            raise self.bot.errors.UwUTurnedOff(self.bot.config["uwu_channel"])

        async def image():
            p = "usercontent/images/uwu/"
            img = p + random.choice(os.listdir(p))
            msg = random.choice(["uwu", "UwU", "OwO", "ÒwÓ", "ÙwÚ", "ÓwÒ", "^w^", ":3"])
            await ctx.send(msg, file=discord.File(img))
            self.logger.log("info", "uwu", f"Sent {img} to #{ctx.channel}")

        async def text():
            await ctx.send(random.choice(self.replies["uwu"]))

        roulette = [image, text]
        await random.choice(roulette)()

    @commands.command(name="pain", brief="Epic programur bnan moments")
    @commands.cooldown(1, settings["pain_cooldown"], BucketType.user)
    async def pain(self, ctx):
        p = "usercontent/images/pain"
        img = p + random.choice(os.listdir(p))
        msg = random.choice(["*pain.*", "*cri*", "not proud of that one", "very bigbrein moment", "so dumb smh", "mf"])
        await ctx.send(msg, file=discord.File(img))
        self.logger.log("info", "pain", f"Sent {img} to #{ctx.channel}")


def setup(bot):
    bot.add_cog(BotInfo(bot))
