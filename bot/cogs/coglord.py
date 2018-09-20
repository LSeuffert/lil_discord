import discord
import json, urllib.request
from discord.ext import commands
import random

class CogLord:
    def __init__(self, bot):
        self.bot = bot
        self.quoteurl = 'http://lil-discord.herokuapp.com/quotes'

    @commands.command()
    async def test(self):
        await self.bot.say('Test message.')

    @commands.command()
    async def quote(self):
        #Matthew's quote
        await self.bot.say(self.get_quote())

    @commands.command()
    async def echo(self, *args):
        print(args)
        await self.bot.say(' '.join(args))

    @commands.command(pass_context=True)
    async def lil(self, ctx):
        await self.bot.say('lil '+ctx.message.author.name)

    def get_quote(self):
        with urllib.request.urlopen(self.quoteurl) as url:
            data = json.loads(url.read().decode())
            return data['quote']

def setup(bot):
    bot.add_cog(CogLord(bot))
