import configparser

class Config():
    def __init__(self):
        conf = configparser.ConfigParser(interpolation=None)
        conf.read('config/config.ini', encoding='utf-8')
        self.discord_token = conf.get('Credentials', 'DiscordToken')
        self.prefix = conf.get('General', 'Prefix')
        self.auth = (self.discord_token,)
