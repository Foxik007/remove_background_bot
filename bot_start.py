import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.handlers.echo import register_echo
from tgbot.handlers.menu import register_menu
from tgbot.handlers.user import register_user

logger = logging.getLogger(__name__)

#Регистрируем хендлеры
def register_all_handlers(dp):
    register_menu(dp)
    register_user(dp)
    register_echo(dp)


config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    #Без редиса используем MemoryStorage
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()

    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
