from managers import logger
from pathlib import Path
import os
import signal
import subprocess

main_path = Path(__file__).resolve().parent
paths = [
	Path(main_path, "bots", "vk"),
	Path(main_path, "bots", "tg"),
	Path(main_path, "bots", "ds")
]
processes = []

def start() -> None: # Как нибудь сделаю запуск ботов эффективнее... А щяс пока что так
	try:
		for path in paths:
			logger.info(f"Проверка и установка зависимостей \"{path}\"...")
			subprocess.call(f"cd {path} && poetry install", shell = True)
			processes.append(subprocess.Popen(f"cd {path} && poetry run python bot.py {main_path}", shell = True))

		for process in processes:
			process.wait()

	except KeyboardInterrupt:
		for process in processes:
			process.send_signal(signal.SIGINT)

if __name__ == "__main__":
	start()