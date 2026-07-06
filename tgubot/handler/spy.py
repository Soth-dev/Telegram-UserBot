from telethon import events
from traceback import format_exc as ERR

HANDLERS = []
FUNCS = []


def SPY(**a):
    """
    Decorator to register a handler for both edited and new messages.
    Optional: p="regex" for case-insensitive pattern.
    """

    if "pattern" in a:
        t: str = a["pattern"]
        if t.startswith("(?s)"):
            t = t[4:]
        if t.startswith("^"):
            t = t[1:]
        # if t.endswith("$"):
        #     t = t[:-1]
        FUNCS.append(t)

    print(
        f"  \033[93mFunction:\033[0m {a['pattern'] if 'pattern' in a else '\033[96m(any)\033[0m'}{' \033[96m(outgoing)\033[0m' if 'outgoing' in a and a['outgoing'] else ''}"
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
                print(
                    f"\033[101m\033[93m[SPY]\033[0m\033[91m Handler error:\033[0m\n{ERR()}"
                )

        HANDLERS.append((wrapper, events.NewMessage(**a)))
        HANDLERS.append((wrapper, events.MessageEdited(**a)))
        return wrapper

    return decorator
