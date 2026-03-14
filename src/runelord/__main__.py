import os
import dotenv
from runelord.bot import create_bot


def main():
    dotenv.load_dotenv()
    token = os.environ["DISCORD_TOKEN"]
    bot = create_bot()
    bot.run(token)


if __name__ == "__main__":
    main()
