import asyncio

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from python.config import bToken
from python.handlers.message_handlers import register_message_handlers
from python.handlers.query_handlers import register_query_handlers


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        [BotCommand(command="/start", description='Start Command'),  # start
         BotCommand(command="/que", description='Give Answers :)'),  # que
         BotCommand(command="/ans", description='Check UR Answers'),  # ans
         BotCommand(command="/del", description='Delete UR Answers'),  # del
         ]
    )


async def main():
    bot = Bot(token=bToken)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # HANDLERS
    register_message_handlers(dp)
    register_query_handlers(dp)

    # УСТАНОВКА КОМАНД
    await set_commands(bot)

    # ПОЛЛИНГ
    await dp.start_polling()


if __name__ == '__main__':
    print('Bot started')
    asyncio.run(main())
