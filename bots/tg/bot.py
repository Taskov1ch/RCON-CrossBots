import argparse
import os
import sys

parser = argparse.ArgumentParser(description = "To get the working directory")
parser.add_argument("main_path", type = str, help = "Working directory")
args = parser.parse_args()
sys.path.append(args.main_path)
os.chdir(args.main_path)

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from managers import config, logger
from routers import all
import asyncio
import os

async def on_startup(bot: Bot) -> None:
	logger.info("Telegram bot is working")

load_dotenv()
bot = Bot(token = os.getenv("TG_TOKEN"))
dp = Dispatcher()
dp.startup.register(on_startup)

for router in all:
	dp.include_routers(router)

async def run() -> None:
	await bot.delete_webhook(drop_pending_updates = True)
	await dp.start_polling(bot)

if __name__ == "__main__":
	if config("tg_config")["enabled"]:
		asyncio.run(run())
