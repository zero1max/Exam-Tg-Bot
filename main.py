import asyncio, sys, logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_all_handlers
from tortoise import Tortoise
from config import init_db


async def main():
    await init_db()
    try:
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()
        register_all_handlers(dp)
        await dp.start_polling(bot)
    finally:
        await Tortoise.close_connections()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
