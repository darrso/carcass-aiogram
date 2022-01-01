from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSMBot.python.States.Questions import Questionss
from FSMBot.python.buttons.bttns import first_que
from FSMBot.python.buttons.inline_bttns import third_ques


async def start_command(message: types.Message):
    await message.answer("If you would like to answer questions, please send /que")


async def questions(message: types.Message):
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


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(questions, commands="que", state="*")
    dp.register_message_handler(second_que, state=Questionss.que)
    dp.register_message_handler(third_que, state=Questionss.quee)
