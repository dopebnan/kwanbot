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


class General(commands.Cog, name="General", description="Legacy fun stuff"):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger
        self.replies = bot.config["general"]

    @commands.command(name="pic", brief="Out of context pictures innit")
    @commands.cooldown(1, settings["pic_cooldown"], BucketType.user)
    async def pic(self, ctx, sub="all"):
        if sub not in os.listdir('usercontent/images/pic/') and sub != "all":
            raise self.bot.errors.BadArgument("WhO'S tHaT??!", sub)
        if sub == 'all':
            imgs = []
            for path, subdirs, files in os.walk("usercontent/images/pic"):
                for name in files:
                    imgs.append(os.path.join(path, name))
            img = random.choice(imgs)
        else:
            p = "usercontent/images/pic/" + sub + '/'
            img = p + random.choice(os.listdir(p))
        msg = random.choice(["remember this:", "bruh", "pic pog"])
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
                imgs = []
                for path, subdirs, files in os.walk("usercontent/images/pic"):
                    for name in files:
                        imgs.append(os.path.join(path, name))
                img = random.choice(imgs)
                msg = random.choice(["remember this:", "bruh", "pic pog"]) + f" ({j + 1}/{i})"
                await ctx.send(msg, file=discord.File(img))
                self.logger.log("info", "autopic", f"Sent {img} to #{ctx.channel} ({j + 1}/{i})")
                await asyncio.sleep(settings["autopic_sleep"])

    @commands.command(name="succ", brief="HOLI BUSSY PRAYERZ SUCCSUCCSUCC")
    async def succ(self, ctx):
        await ctx.send(random.choice(self.replies["succ"]))

    @commands.command(name="brit", brief="GOD SAVE THE QUEEEN")
    async def brit(self, ctx):
        await ctx.send(random.choice(self.replies["brit"]))

    @commands.command(name="uwu", aliases=["heresy", "cappybs"], brief="Only the Finest Cappy Bullshit™ 24/7")
    @commands.cooldown(1, settings["uwu_cooldown"], BucketType.user)
    async def uwu(self, ctx):
        if ctx.channel.id != self.bot.config["uwu_channel"] and not settings["uwu_bool"]:
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
        p = "usercontent/images/pain/"
        img = p + random.choice(os.listdir(p))
        msg = random.choice(["*pain.*", "*cri*", "not proud of that one", "very bigbrein moment", "so dumb smh", "mf"])
        await ctx.send(msg, file=discord.File(img))
        self.logger.log("info", "pain", f"Sent {img} to #{ctx.channel}")

    @commands.command(name="compliment", brief="Jusi compliments")
    @commands.cooldown(1, 30, BucketType.user)
    async def compliment(self, ctx):
        msg = random.choice(self.replies["compliment"])
        await ctx.send(msg)

    @commands.command(name="add_to_cart", aliases=["buy", "add", "cart"], brief="Buy something")
    @commands.cooldown(5, 86400, BucketType.user)
    async def add_to_cart(self, ctx, item=None):
        usr = ctx.message.author.id

        if not os.path.isfile("usercontent/carts.json"):
            with open("usercontent/carts.json", 'w') as f:
                f.write("{}")

        with open("usercontent/carts.json", 'r') as carts:
            cart = json.load(carts)

        if str(usr) not in cart:
            cart[str(usr)] = []

        if item:
            cart[str(usr)].append(item)
            with open("usercontent/carts.json", 'w') as f:
                json.dump(cart, f)
                embed = discord.Embed(
                    title=f"Added ***{item}*** to your cart!",
                    description="Thank you for your purchase!",
                    color=discord.Color.random()
                )
        else:
            embed = discord.Embed(
                description=f"***<@{usr}>'s cart***",
                color=discord.Color.random()
            )
            for i in cart[str(usr)]:
                embed.add_field(name=i, value="\u200b")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
