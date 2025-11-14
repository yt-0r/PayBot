import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import router
from config import settings

from utils.log_config import bot_logger as logger


async def main():
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML,)
    )

    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Starting bot...")
    asyncio.run(main())
