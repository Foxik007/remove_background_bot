from aiogram import Dispatcher, types
from aiogram.bot import bot
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from rembg import remove
from PIL import Image
from pathlib import Path



async def menu(message: types.Message):
    await message.answer('Отправь мне фотографию')

async def donate(message: types.message):
    await message.answer('💸Поддержать проект вы можете:\n'
                         'Сбербанк: 4444-5555-6666-777\n'
                         'Тинькоф:9999-9999-9999-0000')
def register_menu(dp:Dispatcher):
    dp.register_message_handler(donate,Text(equals='💸Сказать спасибо'))

