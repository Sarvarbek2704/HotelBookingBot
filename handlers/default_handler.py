from aiogram import types
from bot import dp


@dp.message_handler(state='*', content_types=types.ContentTypes.ANY)
async def send_default_message(message: types.Message):
        await message.answer('Sorry, I can not parse your command, there is an input error')
