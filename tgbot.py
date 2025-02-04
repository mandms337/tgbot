import asyncio
import logging

from aiogram import Dispatcher, Bot, Router, F
from aiogram.filters import Command



router = Router(name='MyRouter')


@router.message(Command('start', 'Привет'))


async def main():
    bot = Bot(token='7581915376:AAG8FWud6rpdfM7tRhVgaWmz19-AeX9Gogg')
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
asyncio.run(main())
