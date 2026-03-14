from dotenv import load_dotenv

load_dotenv(".env")

import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from logging import INFO, basicConfig, getLogger
from .handler.spy import HANDLERS
from tgubot import function


def main():
    # print(func_pkg.__path__)
    # print(lib.__path__)
    # print(importlib.util.find_spec(*lib.__path__))
    # print(os.listdir(*lib.__path__))
    # return
    fix()

    basicConfig(format="%(message)s", level=INFO)
    LOGS = getLogger(__name__)

    string_session = os.getenv("STRING_SESSION")
    api_id = os.getenv("API_KEY")
    api_hash = os.getenv("API_HASH")

    # print(string_session, api_id, api_hash)
    if not all([string_session, api_id, api_hash]):
        LOGS.error("Missing one or more required environment variables.")
        return

    bot = TelegramClient(StringSession(string_session), api_id, api_hash)

    # Attach all collected handlers
    for callback, builder in HANDLERS:
        bot.add_event_handler(callback, builder)
        print(dir(callback), dir(builder))
    # print(HANDLERS)

    bot.start()
    LOGS.info("BOT ON")
    bot.run_until_disconnected()
    LOGS.info("BOT OFF")

def fix():
    for i in [".cache","saved"]:
        if not os.path.exists(f"./{i}"):
            os.mkdir(f"./{i}")

if __name__ == "__main__":
    main()
