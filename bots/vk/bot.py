import argparse
import os
import sys

parser = argparse.ArgumentParser(description = "Для получения рабочего каталога")
parser.add_argument("main_path", type = str, help = "Рабочий каталог")
args = parser.parse_args()
sys.path.append(args.main_path)
os.chdir(args.main_path)

from dotenv import load_dotenv
from handlers import all
from managers import config, logger
from vkbottle import BuiltinStateDispenser
from vkbottle.bot import Bot

logger.disable("vkbottle")

load_dotenv()
bot = Bot(token = os.getenv("VK_TOKEN"))
for lb in all:
	bot.labeler.load(lb)

if __name__ == "__main__":
	if config("vk_config")["enabled"]:
		logger.info("ВК бот запускается...")
		bot.run_forever()