"""
from telethon import events
from main import bot
def SPY(**a):
    p = a.get('p', None)
    if p: a['pattern'] = '(?i)' + p
    def d(f):
        async def w(c):
            try: await f(c)
            except KeyboardInterrupt: pass
        bot.add_event_handler(w, events.MessageEdited(**a))
        bot.add_event_handler(w, events.NewMessage(**a))
        return w
    return d
"""
# tgubot/func/spy.py
from telethon import events

HANDLERS = []

def SPY(**a):
    """
    Decorator to register a handler for both edited and new messages.
    Optional: p="regex" for case-insensitive pattern.
    """
    p = a.pop("p", None)
    if p: a["pattern"] = "(?i)" + p

    def decorator(func):
        async def wrapper(E):
            try:
                await func(E)
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print(f"[SPY] Handler error: {e}")

        HANDLERS.append((wrapper, events.NewMessage(**a)))
        HANDLERS.append((wrapper, events.MessageEdited(**a)))
        return wrapper

    return decorator