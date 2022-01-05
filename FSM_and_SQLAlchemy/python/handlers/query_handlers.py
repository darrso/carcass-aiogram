from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from FSMBot.python.States.Questions import Questionss
from FSM_and_SQLAlchemy.python.SQLite.connect import session, User


async def end(query: types.CallbackQuery, state: FSMContext):
    await state.update_data(living=query.data)
    data = await state.get_data()
    await query.message.answer("Ok... Your answers:\n"
                               f"Name: {data['name']}\n"
                               f"Old: {data['old']}\n"
                               f"Do u like living? Your answer: {data['living']}")
    try:
        session.add(User(TgId=query.from_user.id, Name=data['name'], Old=data['old'], Living=data['living']))
        session.commit()
    except:
        await query.message.answer('You have already answered the questions! You can view your answers with /ans')
        session.rollback()  # Я НЕ УВЕРЕНА В ЭТОМ

    await state.finish()


def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(end, state=Questionss.queee)
