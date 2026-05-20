from html import escape as FIX
from traceback import format_exc as ERR
from telethon.events import NewMessage
from telethon.tl.custom import Message

CORE = {
    "SUDO": "./saved/sudo",
    "ISUDO": "./saved/isudo",
    "DMUTE": "./saved/dmute",
}

"""Strings"""
AFTER_DMUTE = "Now I may shut you up when I can, {}"
AFTER_DMUTE_NUKE = "I will stop trying to shut you up, {}"
AFTER_SUDO = "Now you have a protected access to my shell, {}"
AFTER_SUDO_NUKE = "You no longer have a protected access to my shell, {}"
AFTER_ISUDO = "Now you have full access to my shell, {}"
AFTER_ISUDO_NUKE = "You no longer have full access to my shell, {}"
NOT_THERE = "This user's not there anyway"
ALREADY_THERE = "This user's already there"

"""Fix Missing Files"""
[open(CORE[f], "a").close() for f in CORE]

"""Get, Edit, Inspect & Send Messages"""


def ARG(E: NewMessage.Event, n: int) -> str:
    return E.pattern_match.group(n) if E.pattern_match else ""


async def GR(E: NewMessage.Event) -> Message | None:
    return await E.get_reply_message()


async def ED(E: NewMessage.Event, t):
    try:
        return await E.edit(t, parse_mode="HTML")
    except Exception as ex:
        if "not modified" in str(ex):
            pass
        else:
            return await SM(
                E, E.chat_id if hasattr(E, "chat_id") else E.peer_id.channel_id, t
            )


async def SM(E: NewMessage.Event, id, t):
    return (
        await E.client.send_message(id, t, parse_mode="HTML")
        if E.client and hasattr(E.client, "send_message")
        else None
    )


def QT(E: NewMessage.Event):
    return E.reply_to.quote_text


def T(E: NewMessage.Event | Message | None) -> str | None:
    return (
        None
        if not E
        else E.text
        if hasattr(E, "text")
        else getattr(E.message, "text", None)
    )


"""Obtain ID, User, Entity & Info"""


async def EN(E: NewMessage.Event, id):
    return (
        await E.client.get_entity(int(id))
        if E.client and hasattr(E.client, "get_entity")
        else None
    )


def U(EN, i=0):
    return EN.username if not i else (EN.username, EN.first_name)


def ID(E: NewMessage.Event | Message) -> int:
    return E.sender_id


"""Execute & Get SUDO"""


"""
def SU(C):
    try:
        o = FIX(SSU(C).stdout.read())
    except Exception as e:
        o = F(FIX(0), "blockquote") + f"{e}" + F(None, "blockquote")
    if len(o) + len(C) >= 4000:
        o = f"{M(o[: 4000 - len(C)])}{F(0, 'blockquote')}\n{Q(M('[CUT OUTPUT TO ' + str(4000 - len(C)) + '/' + str(len(o) + len(C)) + ' CHARS; NO MORE SPACE]'))}{F([], 'blockquote')}"
    return Q(M("$ ") + M(C) + M("\n" + o if o else ""))
"""


def GS():
    return EYE("SUDO")


def GIS():
    return EYE("ISUDO")


def GDM():
    return EYE("DMUTE")


"""Markdown"""


def F(t, u):
    return f"<{u}>{t}</{u}>" if t else f"</{u}><{u}>" if t == 0 else f"</{u}>"


def Q(t):
    return F(t, "blockquote")


def M(t):
    return F(t, "code")


def P(t):
    return F(t, "pre")


"""Read, Write & Append"""


def PIN(n, t):
    with open(CORE[n], "w") as f:
        f.write(t)


def PEN(n, t):
    with open(CORE[n], "a") as f:
        f.write(t)


def EYE(n):
    with open(CORE[n]) as f:
        return f.read().strip().split("\n")
