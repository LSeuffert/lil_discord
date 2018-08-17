import asyncio
from .config import Config
from discord.ext import commands

class LilDiscord(commands.Bot):
    def __init__(self):
        self.config = Config()
        super().__init__(command_prefix=self.config.prefix)
        self.description="hello"
        
    def run(self):
        try:
            self.loop.run_until_complete(self.start(*self.config.auth))
        except discord.errors.LoginFailure:
            raise exceptions.HelpfulError("Cannot login")

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
 
