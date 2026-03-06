from tgubot.handler.spy import SPY
@SPY(outgoing=True, pattern="!!hello")
async def greet(E):
    await E.reply("Hi there!")