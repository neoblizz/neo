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
    """Shoutout"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def shoutout(self, ctx, twitch : str):
        """Shoutout"""
        
        username = twitch
        bash = "./kraken.sh %s > kraken.log" % twitch
        process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        data = json.loads(output.decode("utf-8"))
        logo = data["users"][0]["logo"]
        bio = data["users"][0]["bio"]
        auth = ctx.message.author
        pprint(logo)
        pprint(bio)
        pprint(twitch)
        pprint(username)
        # data = discord.Embed(colour=discord.Colour(0x942be2), url=username, description="Twitch profile.")
        # data.set_thumbnail(url=logo)
        # data.set_author(name=username, url=username)
        # data.add_field(name="Biography", value=bio) 
        # await self.bot.say(embed=data)

def setup(bot):
    bot.add_cog(Shoutout(bot))
