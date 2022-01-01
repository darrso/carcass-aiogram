from aiogram import types, Dispatcher

from Buttons.python.buttons.bttns import yes_no


async def yes(query: types.CallbackQuery):
    await query.message.answer("YO! U pressed yes?", reply_markup=yes_no)


async def no(query: types.CallbackQuery):
    await query.message.answer("YO! U pressed no?", reply_markup=yes_no)


def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(yes, text='yes')
    dp.register_callback_query_handler(no, text='no')
