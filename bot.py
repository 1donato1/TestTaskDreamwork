import os.path
from os import path
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from aiogram.filters.command import CommandObject


import config as cfg

class BotMethods:
    '''
    Contains instructions that process various events.
    '''

    def validate_traking_channel(self,channel):
        if channel[0:5] != 't.me/':
            raise ValueError('Channel must start on t.me/')


    
    def load_all_dp(self):

        @self.dp.message(Command("test1"))
        async def cmd_test1(message: types.Message):
            await message.reply("Test 1")


        # print all
        @self.dp.message(Command("test2"))
        async def cmd(message: types.Message):
            counter = 1
            for i in cfg.traking_channels:
                
                await message.answer(f'{counter} : {i}')
                counter += 1

        # add new
        @self.dp.message(Command('test3'))
        async def cmd(message: types.Message, command : CommandObject):
            
            args = command.args.split()
            new_channel = args[0].replace('https://','')
            try:
                self.validate_traking_channel(new_channel)
                cfg.traking_channels.append(new_channel)
                await message.answer(f'New channel in list : {new_channel}')
            except:
                await message.answer('Некоректний ввід!')

        # delete
        @self.dp.message(Command('test4'))
        async def cmd(message: types.Message, command : CommandObject):
            
            args = command.args.split()
            print(args)
            try:
                del cfg.traking_channels[int(args[0])-1]
            except:
                await message.answer(f'Невдалося видалити позицію {args[0]}')

        


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