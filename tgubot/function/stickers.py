from telethon.events import NewMessage
from tgubot.plugin.functions import ARG
from tgubot.handler.spy import SPY


@SPY(pattern="^!!stick add (\\S+) (.+)", outgoing=True)
async def mksticker(E: NewMessage.Event):
    link, emoji = ARG(E, 1), ARG(E, 2)
    await E.edit(f"Link: {link}\nEmoji: {emoji}")
