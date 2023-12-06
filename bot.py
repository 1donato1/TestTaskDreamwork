import os.path
from os import path
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


class BotMethods:
    '''
    Contains instructions that process various events.
    '''
    def load_all_dp(self):
        @self.dp.message(Command("test1"))
        async def cmd_test1(message: types.Message):
            await message.reply("Test 1")

        @self.dp.message(Command("test2"))
        async def cmd_test1(message: types.Message):
            await message.reply("Test 2")
    

class BotStart(BotMethods):

    '''
    Reading token and starting bot.
    '''

    def __init__(self) -> None:
        if path.exists("token.txt"):
            with open('token.txt') as f :
                self.token = f.read()
            print('The token was found!')
        else:
            print('Token was not found : ')
            self.token = input('Enter token: ')

        self.dp = Dispatcher()
        print(self.token)
        self.bot = Bot(token=self.token)

    async def start(self):
        self.load_all_dp()
        await self.dp.start_polling(self.bot)
    

        

if __name__ == '__main__':
    client = BotStart()
    asyncio.run(client.start())