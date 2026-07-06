from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ED, Q, M, PEN, PIN, ID, GIS, GS, GDM, GR, U, EN

ADD_SUDO_TRIG = r"^!!TAKE SUDO$"
NUKE_SUDO_TRIG = r"^!!NUKE SUDO$"
ADD_ISUDO_TRIG = r"^!!TAKE ISUDO$"
NUKE_ISUDO_TRIG = r"^!!NUKE ISUDO$"
ADD_DMUTE_TRIG = r"^!!TAKE DMUTE$"
NUKE_DMUTE_TRIG = r"^!!NUKE DMUTE$"
"""Strings"""
AFTER_DMUTE = "Now I may shut you up when I can, {}"
AFTER_DMUTE_NUKE = "I will stop trying to shut you up, {}"
AFTER_SUDO = "Now you have a protected access to my shell, {}"
AFTER_SUDO_NUKE = "You no longer have a protected access to my shell, {}"
AFTER_ISUDO = "Now you have full access to my shell, {}"
AFTER_ISUDO_NUKE = "You no longer have full access to my shell, {}"
NOT_THERE = "This user's not there anyway"
ALREADY_THERE = "This user's already there"
"""Add SUDO"""


@SPY(outgoing=True, pattern=ADD_SUDO_TRIG)
async def add_sudo(E):
    if not E.is_reply:
        return
    id = ID(await GR(E))
    if str(id) in GS():
        await ED(E, Q(M(ALREADY_THERE)))
        return
    PEN("SUDO", "\n" + str(id))
    await ED(E, Q(M(AFTER_SUDO.format(U(await EN(E, id))))))


"""Nuke SUDO"""


@SPY(outgoing=True, pattern=NUKE_SUDO_TRIG)
async def nuke_sudo(E):
    if not E.is_reply:
        return
    id = ID(await GR(E))
    if str(id) not in GS():
        await ED(E, Q(M(NOT_THERE)))
        return
    old = GS()
    new = [l for l in old if str(id) not in l]
    PIN("SUDO", "\n".join(new))
    await ED(E, Q(M(AFTER_SUDO_NUKE.format(U(await EN(E, id))))))


"""Nuke ISUDO"""


@SPY(outgoing=True, pattern=NUKE_ISUDO_TRIG)
async def nuke_isudo(E):
    if not E.is_reply:
        return
    id = ID(await GR(E))
    if str(id) not in GIS():
        await ED(E, Q(M(NOT_THERE)))
        return
    old = GIS()
    new = [l for l in old if str(id) not in l]
    PIN("ISUDO", "\n".join(new))
    await ED(E, Q(M(AFTER_ISUDO_NUKE.format(U(await EN(E, id))))))


"""Add ISUDO"""


@SPY(outgoing=True, pattern=ADD_ISUDO_TRIG)
async def add_isudo(E):
    if not E.is_reply:
        return
    id = ID(await GR(E))
    if str(id) in GIS():
        await ED(E, Q(M(ALREADY_THERE)))
        return
    PEN("ISUDO", "\n" + str(id))
    await ED(E, Q(M(AFTER_ISUDO.format(U(await EN(E, id))))))


"""Add Dmute"""


@SPY(outgoing=True, pattern=ADD_DMUTE_TRIG)
async def add_dmute(E):
    if not E.is_reply:
        return
    id = ID(await GR(E))
    PEN("DMUTE", "\n" + str(id))
    await ED(E, Q(M(AFTER_DMUTE.format(U(await EN(E, id))))))


"""Nuke Dmute"""


@SPY(outgoing=True, pattern=NUKE_DMUTE_TRIG)
async def nuke_dmute(E):
    if not E.is_reply:
        return
    id = ID(await GR(E))
    if str(id) not in GDM():
        await ED(E, Q(M(NOT_THERE)))
        return
    old = GDM()
    new = [l for l in old if str(id) not in l]
    PIN("DMUTE", "\n".join(new))
    await ED(E, Q(M(AFTER_DMUTE_NUKE.format(U(await EN(E, id))))))
