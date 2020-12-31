#t.me/ThirdsemBot

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

PROXY_URL = 'socks5://176.59.35.162' # вставить здесь подходящий ip

secret_token = '1286383995:AAFiE2W8qB2K2Kgodyr9vbx7KnI82Iz90xY'

bot = Bot(token=secret_token, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)