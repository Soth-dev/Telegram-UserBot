from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from datetime import datetime


@SPY(outgoing=True, pattern="!!ping$")
async def ping(E: NewMessage.Event):
    start = datetime.now()
    await E.edit("Checking Ping.....")
    end = (datetime.now() - start).microseconds / 1000
    repl_msg = await E.get_reply_message()
    if repl_msg:
        await repl_msg.reply(f"Pong! {end} ms.")
    else:
        await E.reply(f"Pong! {end} ms.")
    await E.delete()
