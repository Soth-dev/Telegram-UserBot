from tgubot.handler.spy import SPY


async def Greet(E):
    await E.reply("Hi there!")


SPY(outgoing=True, pattern="^!!hello$")(Greet)
# SPY(outgoing=True, pattern="^/start$")(Greet)
