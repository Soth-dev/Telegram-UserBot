from telethon.events import NewMessage
from tgubot.handler.spy import FUNCS, SPY
from tgubot.plugin.functions import Q, M, FIX


async def show_cmd(E: NewMessage.Event):
    await E.edit(
        "All command:\n" + Q("\n".join(M(FIX(n)) for n in FUNCS)), parse_mode="HTML"
    )


SPY(pattern="^!!help$", outgoing=True)(show_cmd)
SPY(outgoing=True, pattern="^!!cmd$")(show_cmd)
