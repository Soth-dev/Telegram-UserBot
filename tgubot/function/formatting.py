from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ARG, GR, T, QT


@SPY(outgoing=True, pattern="(?s)^!!html ?(.+)?")
async def html(E: NewMessage.Event):
    a = ARG(E, 1)
    reply = QT(E) if E.reply_to and E.reply_to.quote else T(await GR(E))
    await E.edit(a if a != "" else reply, parse_mode="HTML")
