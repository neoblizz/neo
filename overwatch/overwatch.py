# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from random import randint
import aiohttp

__author__ = "Neoblizz"


class Overwatch:
    """Statistics for Overwatch"""

    def __init__(self, bot):
        self.bot = bot
        self.header = {"User-Agent": "User_Agent"}
        self.api = None

    @commands.command(aliases=["ow"], pass_context=True)
    async def overwatch(self, ctx, username, xbox_ps4: str = None):
        """Overwatch Stats

        If you have a space in your name use quotations"""
        m = ctx.message
        user = username.replace("#", "-")
        url = "https://owapi.net/api/v3/u/"
        # if "patch" == username.lower():
        #     await self.patch(ctx)
        # else:
        async with aiohttp.ClientSession(headers=self.header) as session:
            if xbox_ps4 is None or xbox_ps4.lower() == "pc":
                platform = "pc"
                region = "us"
            elif xbox_ps4.lower() == "xbox":
                platform = "xbl"
                region = "global"
            elif xbox_ps4.lower() == "ps4":
                platform = "psn"
                region = "global"
            else:
                await self.bot.say("Trouble reading the platform type. \n<pc/xbox/ps4> or missing quotes around name")
                return
            fetch = await self.bot.send_message(m.channel, ":clipboard: Fetching player data for " + username + "...")
            owapicall = url + user + "/" + "stats" + "?" + "platform=" + platform
            print("OW API INVOKED: ", owapicall)
            if platform == "pc":
                await self.bot.delete_message(fetch)
                await self.bot.say("PC is not supported. :shrug:")                 
            else:
                async with session.get(owapicall) as console:
                    self.api = await console.json()
                    if 'any' in self.api:
                        await self.bot.delete_message(fetch)
                        await self.stats(ctx, username, platform)
                    else:
                        reminder = ""
                        await self.bot.delete_message(fetch)
                        await self.bot.say(username + " not found. \nUser is cap-sensitive" + reminder)

    async def stats(self, ctx, username, platform):
        m = ctx.message
        data = self.api['any']
        qp = "Games Won - " + str(data['stats']['quickplay']['overall_stats'].get('wins', []))\
             + "\nTime Played - " + str(data['stats']['quickplay']['game_stats'].get('time_played', []))\
             + "\nGold Medals - " + str(data['stats']['quickplay']['game_stats'].get('medals_gold', []))\
             + "\nEliminations - " + str(data['stats']['quickplay']['game_stats'].get('eliminations', []))\
             + "\nBest Kill Streak - " + str(data['stats']['quickplay']['game_stats'].get('kill_streak_best', []))
        comp = "SR - " + str(data['stats']['competitive']['overall_stats'].get('comprank', []))\
               + "\nGames Won - " + str(data['stats']['competitive']['overall_stats'].get('wins', []))\
               + "\nGames Lost - " + str(data['stats']['competitive']['overall_stats'].get('losses', []))\
               + "\nGames Played - " + str(data['stats']['competitive']['overall_stats'].get('games', []))\
               + "\nTime Played - " + str(data['stats']['competitive']['game_stats'].get('time_played', []))
        em = discord.Embed(title="Overwatch Stats on " + platform.upper(),
                           colour=randint(0, 0xFFFFFF),
                           description="Rank: " + str(data['stats']['quickplay']['overall_stats']['tier']) + "\nLevel: " + str(data['stats']['quickplay']['overall_stats']['prestige']) + str(data['stats']['quickplay']['overall_stats']['level']))
        em.set_thumbnail(url=str(data['stats']['quickplay']['overall_stats']['avatar']))
        em.set_author(name=username)
        em.set_footer(text="Git Gud~")
        em.add_field(name="Quick Play",
                     value=qp)
        em.add_field(name="Competitive",
                     value=comp)
        em.add_field(name="Lucky Number",
                     value=randint(1, 100))
        await self.bot.send_message(m.channel, embed=em)

    # async def patch(self, ctx):
    #     m = ctx.message
    #     url =
    #     async with aiohttp.ClientSession(headers=self.header) as session:
    #         async with session.get(url) as notes:
    #             self.api = await notes.json()
    #             data = self.api['patchNotes'][0]
    #             await self.bot.send_message(m.channel, str(data['detail']))


def setup(bot):
    n = Overwatch(bot)
    bot.add_cog(n)
