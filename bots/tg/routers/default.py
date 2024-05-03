from .filters import HasPermission
from aiogram import Router, F
from aiogram.types import Message
from managers import config
from rcon import execute

rt = Router()

@rt.message(HasPermission())
async def send_command(message: Message) -> None:
	text = message.text
	prefix = config("tg_config")["prefix"]

	if not text.startswith(prefix) or len(text) == len(prefix):
		return

	command = text[len(prefix):].strip().lower()

	if command.split()[0] in config("main_config")["blocked_commands"]:
		await message.reply(config("main_config")["messages"]["blocked_command"])
		return

	temp_message = await message.reply(config("main_config")["messages"]["sending"])
	answer = await execute(command)
	await temp_message.delete()

	if not answer["status"]:
		await message.reply(config("main_config")["messages"]["error"].format(
			error = answer["answer"]
		))
		return

	answer = config("main_config")["messages"]["answer"].format(
		ping = answer["ping"],
		answer = answer["answer"]
	)
	answer_parts = [answer[i:4000] for i in range(0, len(answer), 4000)]

	for part in answer_parts:
		await message.reply(part)

@rt.message(F.chat.type == "private")
async def send_id(message: Message) -> None:
	await message.reply(config("main_config")["messages"]["not_permission"].format(
		id = message.from_user.id
	))