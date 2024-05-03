from .rules import HasPermission, config
from dotenv import load_dotenv
from os import getenv
from rcon import execute
from vkbottle import API
from vkbottle.bot import BotLabeler, Message

load_dotenv()
api = API(token = getenv("VK_TOKEN"))
lb = BotLabeler()

@lb.message(HasPermission())
async def send_command(message: Message) -> None:

	if not isinstance(message, Message):
		return

	text = message.text
	prefix = config("vk_config")["prefix"]

	if not text.startswith(prefix) or len(text) == len(prefix):
		return

	command = text[len(prefix):].strip().lower()

	if command.split()[0] in config("main_config")["blocked_commands"]:
		await message.reply(config("main_config")["messages"]["blocked_command"])
		return

	temp_message = await message.reply(config("main_config")["messages"]["sending"])
	answer = await execute(command)
	await api.messages.delete(
		delete_for_all = 1,
		peer_id = temp_message.peer_id,
		cmids = temp_message.conversation_message_id
	)

	if not answer["status"]:
		await message.reply(config("main_config")["messages"]["error"].format(
			error = answer["answer"]
		))
		return

	await message.reply(config("main_config")["messages"]["answer"].format(
		ping = answer["ping"],
		answer = answer["answer"]
	))

@lb.private_message()
async def send_id(message: Message) -> None:
	await message.reply(config("main_config")["messages"]["not_permission"].format(
		id = message.from_id
	))