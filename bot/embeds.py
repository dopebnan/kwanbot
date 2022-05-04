"""
kwanCore, a discord.py bot foundation.
Copyright (C) 2022  dopebnan

kwanBot, images not included
Copyright (C) 2022 dopebnan

You should have received a copy of the GNU General Public License
along with kwanCore. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import random

cooldown = ["Slow down there buckaroo", "not so fast", "stop", "cooldown be poopin' them parties", "cooldown rule",
            "no.", "anti-spam caught yo ass", "dam you got arrested for brushing your teeth too fast"]


def command_on_cooldown(seconds):
    embed = discord.Embed(
        title=random.choice(cooldown),
        description=f"***{seconds}s** left of cooldown*",
        color=0xd89a52
    )
    return embed


def command_not_found():
    embed = discord.Embed(
        title="That command doesn't exist",
        description="Better luck next time",
        color=0xE3170A
    )
    return embed
