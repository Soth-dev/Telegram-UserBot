from tgubot.handler.spy import SPY
from tgubot.plugin.functions import GR, ERR


@SPY(outgoing=True, pattern="^/dd$")
async def delete(E):
    try:
        await E.delete()
        await (await GR(E)).delete()
    except Exception:
        print(ERR())
