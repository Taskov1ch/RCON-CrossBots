from dotenv import load_dotenv
from managers import config
from mcrcon import MCRcon
from os import getenv
from time import thread_time

load_dotenv()

async def execute(command: str) -> dict:
	response = {
		"status": False,
		"answer": ""
	}

	try:
		start = thread_time()
		with MCRcon(
			config("main_config")["host"],
			getenv("RCON_PASS"),
			config("main_config")["port"]
		) as rcon:
			rcon.connect()
			answer = rcon.command(command)
		response["status"] = True
		response["answer"] = config("main_config")["messages"]["none_type"] if not answer else answer
		response["ping"] = int((thread_time() - start) * 100) / 100
	except Exception as e:
		response["answer"] = str(e)

	return response