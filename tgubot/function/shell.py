import os
import asyncio
from re import Pattern
from tgubot.plugin import variable
from tgubot.plugin.functions import ID, GS, GIS, Q, M, FIX, ERR
from tgubot.plugin.subshell import SU
from tgubot.plugin.macwin import draw_window
from tgubot.plugin.randomimage import randimg
from tgubot.handler.spy import SPY

MY_USER_ID = os.getenv("MY_USER_ID")


@SPY(pattern="(?s)^!!sh (.*)")
async def Winsh(E):
    id = str(ID(E))
    if id in GS():
        return
    elif id not in GIS() and id != str(MY_USER_ID):
        return
    C = E.pattern_match.group(1)
    print(C)
    if id == str(MY_USER_ID):
        await E.edit(f"{Q(M(f'!!sh {FIX(C)}'))}", parse_mode="HTML")
    try:
        o = SU(C)
    except Exception as e:
        o = f"{e}"
    if len(o) + len(C) >= 4000:
        o = f"{o[: 4000 - len(C)]}\n\n{'[CUT OUTPUT TO ' + str(4000 - len(C)) + '/' + str(len(o) + len(C)) + ' CHARS; NO MORE SPACE]'}"
    finaltext = "$ " + C + "\n" + o if o else f"$ {C}"
    try:
        draw_window("./tgubot/assets/fonts/firacode.ttf", finaltext, randimg()).save(
            "./.cache/wrapped_text_window_with_gradient.png"
        )
        if E.is_reply:
            await E.client.send_file(
                E.chat_id,
                "./.cache/wrapped_text_window_with_gradient.png",
                reply_to=E.reply_to_msg_id,
            )
        else:
            await E.client.send_file(
                E.chat_id,
                "./.cache/wrapped_text_window_with_gradient.png",
                reply_to=E.id,
            )
        if id == str(MY_USER_ID):
            await E.delete()
    except Exception:
        if id == str(MY_USER_ID):
            await E.edit(ERR())
        else:
            await E.reply(ERR())
    os.remove("./.cache/wrapped_text_window_with_gradient.png")


@SPY(pattern="!!shell ?(.+)?")
async def Toggle_shell(E):
    id = str(ID(E))
    if id not in GIS() and id != str(MY_USER_ID):
        return
    # global Shell_ON_T
    C = E.pattern_match.group(1)
    if C:
        try:
            o = SU(C)
        except Exception as e:
            o = f"{e}"
        if len(o) + len(C) >= 4000:
            o = f"{o[: 4000 - len(C)]}\n\n{'[CUT OUTPUT TO ' + str(4000 - len(C)) + '/' + str(len(o) + len(C)) + ' CHARS; NO MORE SPACE]'}"
        finaltext = Q(
            "<code>$ </code><code>" + FIX(C) + "</code>\n" + M(FIX(o))
            if o
            else f"$ {M(FIX(C))}"
        )

        if id == str(MY_USER_ID):
            await E.edit(finaltext, parse_mode="HTML")
        else:
            await E.reply(finaltext, parse_mode="HTML")
    elif E.sender_id == MY_USER_ID:
        if variable.Shell_ON_T:
            variable.Shell_ON_T = False
            await E.edit("<code>SHELL</code>\n\nON\nOFF", parse_mode="HTML")
            await asyncio.sleep(0.3)
            await E.edit(
                "<code>SHELL</code>\n\nON\n<blockquote>OFF</blockquote>",
                parse_mode="HTML",
            )
        else:
            variable.Shell_ON_T = True
            await E.edit("<code>SHELL</code>\n\nON\nOFF", parse_mode="HTML")
            await asyncio.sleep(0.3)
            await E.edit(
                "<code>SHELL</code>\n\n<blockquote>ON</blockquote>\nOFF",
                parse_mode="HTML",
            )
        await asyncio.sleep(5)
        await E.delete()
    else:
        if variable.Shell_ON_T:
            variable.Shell_ON_T = False
            shell_t = await E.reply(
                "ON\n<blockquote>OFF</blockquote>", parse_mode="HTML"
            )
        else:
            variable.Shell_ON_T = True
            shell_t = await E.reply(
                "<blockquote>ON</blockquote>\nOFF", parse_mode="HTML"
            )
        await asyncio.sleep(5)
        await shell_t.delete()
        await E.delete()
