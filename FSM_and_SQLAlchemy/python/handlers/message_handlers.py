from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSMBot.python.States.Questions import Questionss
from FSMBot.python.buttons.bttns import first_que
from FSMBot.python.buttons.inline_bttns import third_ques
from FSM_and_SQLAlchemy.python.SQLite.connect import session, User


async def start_command(message: types.Message):
    await message.answer("If you would like to answer questions, please send /que"
                         "\nFor ur answers /ans")


async def questions(message: types.Message):
    try:
        obj = (session.query(User).filter_by(TgId=message.from_user.id).all())[0].Name
        await message.answer('You have already answered the questions! You can view your answers with /ans')

    except:
        await message.answer("Oh, nice! First question:\n"
                             "How old are you?(choose)", reply_markup=first_que)
        await Questionss.que.set()

async def second_que(message: types.Message, state: FSMContext):
    await state.update_data(old=message.text)
    await message.answer("Ok, next question:\n"
                         "What is your name?", reply_markup=types.ReplyKeyboardRemove())
    await Questionss.next()


async def third_que(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Last:\n"
                         "Do you like living?", reply_markup=third_ques)
    await Questionss.next()


async def your_answers(message: types.Message):
    try:
        data = session.query(User).filter_by(TgId=message.from_user.id).all()
        await message.answer(f'Your answers.\n'
                             f'name:  {data[0].Name}\n'
                             f'old:  {data[0].Old}\n'
                             f'do u like living?  {data[0].Living}'
                             f'\n\nTo delete answers to questions, send /del')
    except IndexError:
        await message.answer("You haven't answered the questions yet!\n"
                             'Send /que')


async def deliting(message: types.Message):
    try:
        obj = session.query(User).filter_by(TgId=message.from_user.id).one()
        session.delete(obj)
        session.commit()
        await message.answer("You have deleted the answers to the questions. To answer again, send /que")
    except:
        await message.answer("You haven't answered the questions yet. Send /que")


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    # --------------------- #
    dp.register_message_handler(questions, commands="que", state="*")
    dp.register_message_handler(second_que, state=Questionss.que)
    dp.register_message_handler(third_que, state=Questionss.quee)
    # --------------------- #
    dp.register_message_handler(your_answers, commands="ans")
    dp.register_message_handler(deliting, commands='del')
