from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from FSMBot.python.States.Questions import Questionss


async def end(query: types.CallbackQuery, state: FSMContext):
    await state.update_data(living=query.data)
    data = await state.get_data()
    await query.message.answer("Ok... Your answers:\n"
                               f"Name: {data['name']}\n"
                               f"Old: {data['old']}\n"
                               f"Do u like living? Your answer: {data['living']}")
    await state.finish()


def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(end, state=Questionss.queee)