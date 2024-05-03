import argparse
import os
import sys

parser = argparse.ArgumentParser(description = "Для получения рабочего каталога")
parser.add_argument("main_path", type = str, help = "Рабочий каталог")
args = parser.parse_args()
sys.path.append(args.main_path)
os.chdir(args.main_path)

# from asyncio import sleep
from discord.ext import commands
from dotenv import load_dotenv
from managers import config, logger
from os import getenv
from rcon import execute
import discord

load_dotenv()
bot = discord.Client(intents = discord.Intents.all())

@bot.event
async def on_ready() -> None:
	logger.info("ДС бот работает")

@bot.event
async def on_message(ctx):
	if ctx.author == bot.user:
		return

	if not discord.utils.get(ctx.author.roles, name = config("ds_config")["role"]):
		return

	allowed_channels = config("ds_config")["channels"]

	if (
		not ctx.channel.name in allowed_channels and
		not "*" in allowed_channels
	):
		return

	text = ctx.content
	prefix = config("ds_config")["prefix"]

	if not text.startswith(prefix) or len(text) == len(prefix):
		return

	command = text[len(prefix):].strip().lower()

	if command.split()[0] in config("main_config")["blocked_commands"]:
		await ctx.reply(config("main_config")["messages"]["blocked_command"])
		return

	temp_ctx = await ctx.reply(config("main_config")["messages"]["sending"])
	answer = await execute(command)
	await temp_ctx.delete()

	if not answer["status"]:
		await ctx.reply(config("main_config")["messages"]["error"].format(
			error = answer["answer"]
		))
		return

	answer = config("main_config")["messages"]["answer"].format(
		ping = answer["ping"],
		answer = answer["answer"]
	)
	await ctx.reply(answer[:2000])

	# answer_parts = [answer[i:1500] for i in range(0, len(answer), 1500)]

	# for part in answer_parts:
	# 	await ctx.reply(part)
	# 	await sleep(1)

if __name__ == "__main__":
	if config("ds_config")["enabled"]:
		bot.run(getenv("DS_TOKEN"), log_handler = None)