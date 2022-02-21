import unittest
from discord_bot_main import *

class TestDiscordBot(unittest.TestCase):

    def init_bot(self):
        client = DiscordClientBot()
        client.start_bot()

if __name__ == '__main__':
    unittest.main()