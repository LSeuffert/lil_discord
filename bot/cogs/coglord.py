import discord
from discord.ext import commands

class CogLord:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self):
        await self.bot.say('Test message.')

    @commands.command()
    async def quote(self):
        #Matthew's quote
        await self.bot.say('I got two questions for you.... do you like anime and do you like hentai? - Matthew')

    @commands.command()
    async def echo(self, *args):
        print(args)
        await self.bot.say(' '.join(args))


def setup(bot):
    bot.add_cog(CogLord(bot))
