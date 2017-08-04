import subprocess
import json
from pprint import pprint

# username = "neoblizz"
# bash = "./kraken.sh %s > kraken.log" % username

# process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()
# data = json.loads(output.decode("utf-8"))
# pprint(data["users"][0]["name"])

import discord
from discord.ext import commands
from random import choice as randchoice

class Shoutout:
    """Display rules statements"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def shoutout(self, ctx, twitch : str):
        """Shoutout statements"""
        
        username = twitch
        bash = "./kraken.sh %s > kraken.log" % username
        process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        data = json.loads(output.decode("utf-8"))
        auth = ctx.message.author
        data = discord.Embed(colour=discord.Colour(0x942be2), url=data["users"][0]["name"], description="Twitch profile.")
        data.set_thumbnail(url=data["users"][0]["logo"])
        data.set_author(name=data["users"][0]["name"], url=data["users"][0]["name"])
        data.add_field(name="Biography", value=data["users"][0]["bio"])
        
        await self.bot.say(embed=data)

def setup(bot):
    bot.add_cog(Shoutout(bot))
