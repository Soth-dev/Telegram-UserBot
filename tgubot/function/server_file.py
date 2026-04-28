from asyncio import sleep
import os

from telethon.events import NewMessage

from tgubot.plugin.functions import T, GR, ED, M, Q, ERR
from tgubot.handler.spy import SPY

DOWNLOAD_TRIG = "!!dl"
UPLOAD_TRIG = "!!ul"


@SPY(outgoing=True, pattern=DOWNLOAD_TRIG)
async def download(E: NewMessage.Event):
    print(type(E))
    t = T(E)
    if not t.startswith(DOWNLOAD_TRIG):
        return
    if not E.is_reply:
        return
    r = await GR(E)
    if not r.media:
        return
    t = t[len(DOWNLOAD_TRIG) + 1 :]
    f = t if t.startswith("/") else os.getcwd() + f"/{t}"

    async def CB(c, t):
        nonlocal E, f
        p = (c / t) * 100
        art = ""
        for i in range(20):
            art += "■" if i * 5 < float(p) else "□"
            c = str(float(c) / 1024 / 1024)[:6]
            t = str(float(t) / 1024 / 1024)[:6]
            p = str(p)[:6]
            pro = f"[{c}MB/{t}MB]"
            await ED(
                E, Q(M(f"{DOWNLOAD_TRIG} ") + M(f) + M(f"\n{pro} {p}%\n") + M(art))
            )

    try:
        await r.download_media(f, progress_callback=CB)
        await sleep(1)
        await sleep(4)
        await E.delete()
    except Exception as e:
        print(ERR())
        await ED(E, Q(M(str(e))))


@SPY(outgoing=True, pattern=UPLOAD_TRIG)
async def upload(E: NewMessage.Event):
    t = T(E)
    if not t.startswith(UPLOAD_TRIG):
        return
    t = t[len(UPLOAD_TRIG) + 1 :]
    f = t if t.startswith("/") else os.getcwd() + f"/{t}"

    async def CB(c, t):
        nonlocal E, f
        p = (c / t) * 100
        art = ""
        for i in range(20):
            art += "■" if i * 5 < float(p) else "□"
        c = str(float(c) / 1024 / 1024)[:6]
        t = str(float(t) / 1024 / 1024)[:6]
        p = str(p)[:6]
        pro = f"[{c}MB/{t}MB]"
        await ED(E, Q(M(f"{UPLOAD_TRIG} ") + M(f) + M(f"\n{pro} {p}%\n") + M(art)))

    try:
        if E.is_reply:
            await E.client.send_file(
                E.chat_id, f, progress_callback=CB, reply_to=E.reply_to_msg_id
            )
        else:
            await E.client.send_file(E.chat_id, f, progress_callback=CB, reply_to=E.id)
        await sleep(1)
        await sleep(4)
        await E.delete()
    except Exception as e:
        await ED(E, Q(M(str(e))))
