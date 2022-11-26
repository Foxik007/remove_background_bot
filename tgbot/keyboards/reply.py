from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


keyboard = ReplyKeyboardMarkup(resize_keyboard=True,)
b1 = KeyboardButton("💸Сказать спасибо", resize_keyboard=True)
keyboard.add(b1)

