from aiogram.filters import BaseFilter
from aiogram.types import Message
from managers import config

class HasPermission(BaseFilter):
	async def __call__(self, message: Message) -> bool:
		return message.from_user.id in config("tg_config")["allowed_ids"]