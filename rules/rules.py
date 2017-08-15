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
        data = discord.Embed(title="Rules and Regulations", description="In order to maintain a thriving community we must maintain the behavior of the community or else nobody will stick around. As such, I present to you a set of rules and regulations which you must follow at all times. If you do not follow these rules, punishments will be mandated.", color=0xff0000)
        data.add_field(name="Offense Behavior:", value="Let's face it, in this day and age people get triggered. We're not saying tread carefully as Team Undead is far from a safe space. However, what I am saying is don't be an asshole. If what you're saying bothers somebody it is their responsibility to tell you to stop. If they tell you to stop then it is your responsibility to stop. It's that fucking simple.", inline=False)
        data.add_field(name="Voice Chats are Sacred:", value="If a person or group of people are using our Voice Chats for gaming, streaming, or the like then do not interfere. If you jump into a stream and start screaming or playing obnoxious music, you will lose your privilege of participating in our VC's for the forseeable future.", inline=False)
        data.add_field(name="Bigotry:", value="It goes without saying that racism, sexism, or disparaging remarks about somebody's religious beliefs will not be tolerated. Feel free to discuss religion as much as you like, but if you start a shit show we will end it.", inline=False)
        data.add_field(name="Spam:", value="Unless initiated by an Admin, you will be kicked. If you come back and continue spamming you will be banned. It's as simple as that. When you're told to stop, you stop.", inline=False)
        data.add_field(name="NSFW:", value="Keep NSFW in #nsfw, only available to members in 18+ (age) usergroup.", inline=False)
        data.add_field(name="Referrals:", value="No referral links without an Admin's approval.", inline=False)
        data.add_field(name="Mentions:", value="Don’t abuse mentions or you will lose your ability to mention.", inline=False)
        data.add_field(name="Arguing:", value="DO NOT argue with staff. This will get you nowhere. If you have a disagreement with a staff member, contact an Admin by DM and respectfully explain your situation. Absolutely do not take things out of context as the Admin will get both sides of the story.", inline=False)
        data.add_field(name="Complaints:", value="If there are repeated complaints about you (within reason), action will be taken.", inline=False)
        data.add_field(name="<3", value="If you feel if any of these rules have been broken, please get in touch with an Admin or Mod ASAP.", inline=False)
        await self.bot.say(embed=data)        

def setup(bot):
    bot.add_cog(Rules(bot))
