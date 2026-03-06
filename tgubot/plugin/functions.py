SHELL_PATH = "/data/data/com.termux/files/usr/bin/bash"
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


async def GR(E, b=0):
    m = await E.get_reply_message()
    return (m, T(m)) if b and m else m if m else (None, None)


async def ED(E, t):
    try:
        return await E.edit(t, parse_mode="HTML")
    except Exception as ex:
        if "not modified" in str(ex):
            pass
        else:
            return await SM(
                E.chat_id if hasattr(E, "chat_id") else E.peer_id.channel_id, t
            )


async def SM(id, t):
    return await bot.send_message(id, t, parse_mode="HTML")


def T(E):
    return E.text if hasattr(E, "text") else E.message.text


"""Obtain ID, User, Entity & Info"""


async def EN(id):
    return await bot.get_entity(int(id))


def U(EN, i=0):
    return EN.username if not i else (EN.username, EN.first_name)


def ID(E):
    return E.sender_id


"""Execute & Get SUDO"""


def SSU(C, **kw):
    return SSSU([SHELL_PATH, "-c", C], stdout=PIPE, stderr=STDOUT, text=True, **kw)


def SU(C):
    try:
        o = FIX(SSU(C).stdout.read())
    except Exception as e:
        o = F(FIX(0), "blockquote") + f"{e}" + F(None, "blockquote")
    if len(o) + len(C) >= 4000:
        o = f"{M(o[: 4000 - len(C)])}{F(0, 'blockquote')}\n{Q(M('[CUT OUTPUT TO ' + str(4000 - len(C)) + '/' + str(len(o) + len(C)) + ' CHARS; NO MORE SPACE]'))}{F([], 'blockquote')}"
    return Q(M("$ ") + M(C) + M("\n" + o if o else ""))


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

