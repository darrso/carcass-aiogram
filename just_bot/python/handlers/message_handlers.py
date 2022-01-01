from aiogram import types, Dispatcher

from just_bot.python.buttons.inline_bttns import start_bttn


async def start_command(message: types.Message):
    await message.answer("Start?\n", reply_markup=start_bttn)


async def yess_noo(message: types.Message):
    await message.answer("Ok", reply_markup=start_bttn)


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(yess_noo, text=['Yes', 'No'])
