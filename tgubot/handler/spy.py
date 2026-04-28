from telethon import events
from traceback import format_exc as ERR

HANDLERS = []


def SPY(**a):
    """
    Decorator to register a handler for both edited and new messages.
    Optional: p="regex" for case-insensitive pattern.
    """
    print(
        f"  \033[93mFunction:\033[0m {a['pattern']}{' \033[96m(outgoing)\033[0m' if 'outgoing' in a else ''}"
    )
    p = a.pop("p", None)
    if p:
        a["pattern"] = "(?i)" + p

    def decorator(func):
        async def wrapper(E):
            try:
                await func(E)
            except KeyboardInterrupt:
                pass
            except Exception:
                print(f"[SPY] Handler error: {ERR()}")

        HANDLERS.append((wrapper, events.NewMessage(**a)))
        HANDLERS.append((wrapper, events.MessageEdited(**a)))
        return wrapper

    return decorator
