
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from tgbot.keyboards.reply import keyboard


async def start(message: Message):
    await message.answer('Отправь мне фотографию с которой нужно убрать фон:😉', reply_markup=keyboard)


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])


