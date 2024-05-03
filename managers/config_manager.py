from os import getcwd
from typing import Union
from yaml import safe_load

path = getcwd() + "/configs"

def config(file_name: str) -> Union[dict, None]:
	try:
		with open(f"{path}/{file_name}.yml", "r", encoding = "utf-8") as file:
			return safe_load(file)
	except Exception as e:
		print(str(e))
		return None