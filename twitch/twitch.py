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
	data = discord.Embed(colour=discord.Colour(0x942be2), url="https://twitch.tv/", description="A")
	data.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/neoblizz-profile_image-8db895b58f67bd79-300x300.jpeg")
	data.set_author(name="NeoBlizz", url="https://discordapp.com")
	data.add_field(name="Aasdfasdf", value="Aasdfasdf")
        
        await self.bot.say(embed=data)

def setup(bot):
    bot.add_cog(Shoutout(bot))
