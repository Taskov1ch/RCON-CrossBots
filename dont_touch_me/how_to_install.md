## 🔌 Prerequisites
Make sure you have everything listed below installed.
* **Python 3.10** or higher
* **Poetry**

If everything is ready, you can proceed with the installation.


## 📥 Installation
1. Move all the source files from this repository to the desired directory on your server (you can do this using **git** or by directly downloading this repository).

2. Navigate to the directory where all the files are located and enter the command `poetry install`. Wait for the installation to finish.

3. Create an environment file **.env** and fill it with the following values:
   - `VK_TOKEN` with the token of your community (bot) from **VKontakte**,
   - `TG_TOKEN` with the token of your bot from **Telegram** ([**@BotFather**](https://t.me/botfather)),
   - `DS_TOKEN` with the token of your bot from **Discord** ([**Discord Applications**](https://discord.com/developers/applications)),
   - `RCON_PASS` with the RCON password of your server.

    You can see an example file [here](env_example.md).

4. Configure all the configuration files in the [**configs**](../configs) directory.

5. After configuration, navigate to the main directory and start the bots with the command `poetry run python loader.py`.
