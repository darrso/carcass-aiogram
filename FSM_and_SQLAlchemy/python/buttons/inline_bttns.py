from aiogram import types

third_ques = types.InlineKeyboardMarkup(row_width=2)

text_and_data = (
    ('Yes', 'yes'), ('No', 'no')
)
third_ques.add(*(types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data))