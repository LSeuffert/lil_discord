import discord
from discord.ext import commands

class CogLord:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self):
        await self.bot.say('Test message.')


def setup(bot):
    bot.add_cog(CogLord(bot))
