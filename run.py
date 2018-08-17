def main():
    from bot import LilDiscord
    lil_discord = LilDiscord()
    load_cogs(lil_discord)
    lil_discord.run()

def load_cogs(bot):
    bot.load_extension('bot.cogs.coglord')
    
if __name__ == '__main__':
    main()
