import asyncio
from util import Config
from discord.ext import commands

class LilDiscord(commands.Bot):
    def __init__(self):
        self.config = Config()
        super().__init__(command_prefix=self.config.prefix)
        self.description="hello"

    async def on_message(self, message):
        lower_message = message.content.lower()

        if message.author == self.user:
            return

        if self.weeb_check(lower_message):
            await self.send_message(message.channel, 'weebs out :angry: :point_right: :door:')
            
        await self.process_commands(message)
        

    def weeb_check(self, msg):
        weeb_index = msg.find('weeb')
        if weeb_index > -1 and (weeb_index == 0 or msg[weeb_index - 1] in ' ') \
           and (weeb_index + 4 >= len(msg) - 1 or msg[weeb_index + 4] in ' s.,!?'):
            return True
        return False
            

        
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
 
