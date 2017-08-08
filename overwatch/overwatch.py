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
            fetch = await self.bot.send_message(m.channel, "Fetching player data for " + username + "..."
                                                + "\n*(This may take awhile)*")
            owapicall = url + user + "/" + "stats" + "?" + "platform=" + platform
            print("OW API INVOKED: ", owapicall)
            async with session.get(owapicall) as us:
                self.api = await us.json()
                if 'any' in self.api:
                    await self.bot.delete_message(fetch)
                    await self.stats(ctx, username, platform)
                else:
                    region = "eu"
                    async with session.get(owapicall) as eu:
                        self.api = await eu.json()
                        if 'any' in self.api:
                            await self.bot.delete_message(fetch)
                            await self.stats(ctx, username, platform)
                        else:
                            region = "kr"
                            async with session.get(owapicall) as kr:
                                self.api = await kr.json()
                                if 'any' in self.api:
                                    await self.bot.delete_message(fetch)
                                    await self.stats(ctx, username, platform)
                                else:
                                    if platform == "pc":
                                        reminder = " and remember to add the bnet tag"
                                    else:
                                        reminder = ""
                                    await self.bot.delete_message(fetch)
                                    await self.bot.say(username + " not found. \nUser is cap-sensitive" + reminder)

    async def stats(self, ctx, username, platform):
        m = ctx.message
        data = self.api['any']
        qp = "Wins - " + str(data['stats']['quickplay']['overall_stats'].get('wins', []))\
             + "\nLost - " + str(data['stats']['quickplay']['overall_stats'].get('losses', []))\
             + "\nPlayed - " + str(data['stats']['quickplay']['overall_stats'].get('games', []))
        comp = "Wins - " + str(data['stats']['competitive']['overall_stats'].get('wins', []))\
               + "\nLost - " + str(data['stats']['competitive']['overall_stats'].get('losses', []))\
               + "\nPlayed - " + str(data['stats']['competitive']['overall_stats'].get('games', []))
        em = discord.Embed(title="Overwatch Stats on " + platform.upper(),
                           colour=randint(0, 0xFFFFFF),
                           description="Level " + str(data['stats']['quickplay']['overall_stats']['prestige']) + str(data['stats']['quickplay']['overall_stats']['level']))
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
