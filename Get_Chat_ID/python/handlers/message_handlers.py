from aiogram import types, Dispatcher


async def start_command(message: types.Message):
    await message.answer("To get the id of this chat, your id - send /id")


async def idd(message: types.Message):
    if message.chat.id == message.from_user.id:
        await message.answer(f"Your(user: {message.from_user.username}) ID:\n{message.from_user.id}")
    else:
        await message.answer(f"Chat ID:\n{message.chat.id}")


# CHANNEL
async def get_channel_id(message: types.Message):
    msg = f"Channel ID:\n{message.forward_from_chat.id}"
    if message.sticker:
        msg += f"\n\nStiker ID:\n{message.sticker.file_id}"
    await message.reply(msg)


# PRIVACY
async def get_user_id_no_privacy(message: types.Message):
    if message.forward_from.is_bot:
        msg = f"Bot ID:\n{message.forward_from.id}"
    else:
        msg = f"User ID:\n{message.forward_from.id}"
    if message.sticker:
        msg += f"\n\nStiker ID:\n{message.sticker.file_id}"
    await message.reply(msg)


async def get_user_id_with_privacy(message: types.Message):
    msg = f"PRIVACY USER ID!"
    if message.sticker:
        msg += f"\n\nStiker ID:\n{message.sticker.file_id}"
    await message.reply(msg)


# __________________________________________________________

def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(idd, commands='id')
    dp.register_message_handler(get_channel_id, lambda message: message.forward_from_chat,
                                content_types=types.ContentTypes.ANY)
    dp.register_message_handler(get_user_id_no_privacy, lambda message: message.forward_from,
                                content_types=types.ContentTypes.ANY)
    dp.register_message_handler(get_user_id_with_privacy, lambda message: message.forward_sender_name,
                                content_types=types.ContentTypes.ANY)
