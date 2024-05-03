from managers import config
from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule

class HasPermission(ABCRule[Message]):
	async def check(self, message: Message) -> bool:
		return message.from_id in config("vk_config")["allowed_ids"]