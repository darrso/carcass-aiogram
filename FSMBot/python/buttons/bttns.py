from aiogram import types
from aiogram.types import KeyboardButton

first_que = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
first_que.add(KeyboardButton('14-18'), KeyboardButton('19-25'), KeyboardButton('26-35'), KeyboardButton('36-50'),
              KeyboardButton('more than 50'))