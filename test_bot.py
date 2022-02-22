import unittest
from discord_bot_main import *

class TestDiscordBot(unittest.IsolatedAsyncioTestCase):

    async def test_init_bot(self):
        client = DiscordClientBot()
        client.start_bot()
        result = await client.start(client.bot_token)
        self.assertTrue(client.is_ready())

if __name__ == '__main__':
    unittest.main()