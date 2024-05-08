import asyncio
from typing import Final
from config import get_config
from pprint import pprint

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import router

async def main():
    # Создаем экземпляр бота
    bot = Bot(token=get_config().bot_token)

    # storage = RedisStorage.from_url('redis://localhost:6379/1', key_builder=DefaultKeyBuilder(with_destiny=True))
    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp.include_routers(router)

    # Отбрасываем сообщения, которые были отправлены боту, пока он был выключен
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main=main())