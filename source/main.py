import logging
from aiogram import Bot, Dispatcher, executor, types

# Get API_TOKEN from .env
from dotenv import load_dotenv
load_dotenv()
import os
API_TOKEN = os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("Hi, I'm AOS!")
    
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    
    await message.reply('No.')

@dp.message_handler()
async def echo(message: types.Message):
    
    if (message.text == '1000-7'):
        text = ''
        for i in range(1000, 0, -7):
            text += f'{i} - 7\n'
        await message.answer(text)
    else:
        await message.answer(message.text)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)