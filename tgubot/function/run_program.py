import io
from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ARG, Q, M, QT, T, GR, FIX
from tgubot.plugin.subshell import SU
from tgubot.plugin.macwin import draw_window
from tgubot.plugin.randomimage import randimg


@SPY(outgoing=True, pattern="(?s)^!!?(i|r)?py ?(.+)?")
async def py(E: NewMessage.Event):
    code = ARG(E, 2)
    reply = QT(E) if E.reply_to and E.reply_to.quote else T(await GR(E))
    if code == "":
        if reply:
            code = reply
        else:
            return
    await E.edit(Q(f"Running {M(FIX(code))}"), parse_mode="HTML")
    with open(".cache/main.py", "w") as f:
        f.write(code)
    r = SU("python .cache/main.py")
    if ARG(E, 1) == "r":
        await E.edit(f"{FIX(r)}"[:4096], parse_mode="HTML")
    elif ARG(E, 1) != "i":
        await E.edit(f"{Q(M(FIX(code)))}\n{Q(M(FIX(r)))}"[:4000], parse_mode="HTML")
    elif E.client:
        with io.BytesIO() as buff:
            draw_window("./tgubot/assets/fonts/firacode.ttf", r[:4000], randimg()).save(
                buff, "PNG"
            )
            buff.name = "image.png"
            buff.seek(0)
            if E.is_reply:
                await E.client.send_file(
                    E.chat_id,
                    buff,
                    caption=Q(M(FIX(code))),
                    parse_mode="HTML",
                    reply_to=E.reply_to_msg_id,
                )
            else:
                await E.client.send_file(
                    E.chat_id,
                    buff,
                    caption=Q(M(FIX(code))),
                    parse_mode="HTML",
                    reply_to=E.id,
                )
        await E.delete()


@SPY(outgoing=True, pattern="(?s)^!!?(i|r)?rs ?(.+)?")
async def rust(E: NewMessage.Event):
    code = ARG(E, 2)
    reply = QT(E) if E.reply_to and E.reply_to.quote else T(await GR(E))
    if code == "":
        if reply:
            code = reply
        else:
            return
    await E.edit(Q(f"Running {M(FIX(code))}"), parse_mode="HTML")
    if "fn main" not in code:
        code = f"fn main() {{\n{''.join(f'    {c}\n' for c in code.split('\n'))}}}"
    with open(".cache/main.rs", "w") as f:
        f.write(code)
    r = SU("rustc .cache/main.rs -o .cache/mainrs && ./.cache/mainrs")
    if ARG(E, 1) == "r":
        await E.edit(f"{FIX(r)}"[:4096], parse_mode="HTML")
    elif ARG(E, 1) != "i":
        await E.edit(f"{Q(M(FIX(code)))}\n{Q(M(FIX(r)))}"[:4000], parse_mode="HTML")
    elif E.client:
        with io.BytesIO() as buff:
            draw_window("./tgubot/assets/fonts/firacode.ttf", r[:4000], randimg()).save(
                buff, "PNG"
            )
            buff.name = "image.png"
            buff.seek(0)
            if E.is_reply:
                await E.client.send_file(
                    E.chat_id,
                    buff,
                    caption=Q(M(FIX(code))),
                    parse_mode="HTML",
                    reply_to=E.reply_to_msg_id,
                )
            else:
                await E.client.send_file(
                    E.chat_id,
                    buff,
                    caption=Q(M(FIX(code))),
                    parse_mode="HTML",
                    reply_to=E.id,
                )
        await E.delete()
