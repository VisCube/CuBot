import os

from discord import Bot, Intents
from dotenv import load_dotenv


def main():
    load_dotenv()

    bot = Bot(intents=Intents.all())
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    main()
