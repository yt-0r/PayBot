import asyncio
from handlers import router
from sheduler.payment_watcher import check_pending_payments
from sheduler.user_watcher import check_users_subscriptions

from utils.log_config import bot_logger as logger
from core.bot_init import bot, dp


async def main():

    dp.include_router(router)

    asyncio.create_task(check_pending_payments())
    asyncio.create_task(check_users_subscriptions())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Starting bot...")
    asyncio.run(main())
