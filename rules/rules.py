import discord
from discord.ext import commands
from random import choice as randchoice

class Rules:
    """Display rules statements"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def rules(self, ctx, user : discord.Member=None):
        """Get rules statements"""
        
        auth = ctx.message.author
        data = discord.Embed(title="Rules and Regulations", description="Oblige these or we'll kill your family.", color=0xff0000)
        data.add_field(name="Rule 1.", value="Don't get offended.", inline=False)
        data.add_field(name="Rule 2.", value="Don't offend others.", inline=False)
        data.add_field(name="Rule 3.", value="Don't bomb gaming VC.", inline=False)
        data.add_field(name="Rule 4.", value="Light/White discord theme is an instant ban.", inline=False)
        await self.bot.say(embed=data)

def setup(bot):
    bot.add_cog(Rules(bot))
