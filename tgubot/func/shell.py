import os
from tgubot.plugin.supshell import SSU
from tgubot.plugin.funcions import ID
MY_USER_ID = os.getenv("MY_USER_ID")
@SPY(pattern="(?s)^!!sh (.*)")
async def winsh(E):
    id = str(ID(E))
    if id in GS(): await E.reply("This feature doesn't work at the moment."); return
    elif id not in GIS() and id != str(MY_USER_ID): return
    C = E.pattern_match.group(1)
    if id == str(MY_USER_ID): await E.edit(f"{Q(M(f'!!sh {FIX(C)}'))}", parse_mode="HTML")
    try: o = SSU(C).stdout.read()
    except Exception as e: o = f"{e}"
    if len(o)+len(C) >= 4000: o = f"{o[:4000-len(C)]}\n\n{'[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'}"
    finaltext = '$ '+C+'\n'+o if o else f'$ {C}'
    try:
        window_image = draw_window("./tgbot/sticker/font/mono.ttf", finaltext, g_image_path())
        window_image.save("wrapped_text_window_with_gradient.png")
        if E.is_reply: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.reply_to_msg_id)
        else: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.id)
        if id==str(MY_USER_ID): await E.delete()
    except Exception:
        if id==str(MY_USER_ID): await E.edit(traceback.format_exc())
        else: await E.reply(traceback.format_exc())
    try: os.remove("wrapped_text_window_with_gradient.png")
    except: pass

@SPY(pattern='!!shell ?(.+)?')
async def toggle_shell(E):
    id = str(ID(E))
    if id not in GIS() and id != str(MY_USER_ID): return
    global Shell_ON_T
    C = E.pattern_match.group(1)
    if C:
        try: o = SSU(C).stdout.read()
        except Exception as e: o = f"{e}"
        if len(o)+len(C) >= 4000: o = f"{o[:4000-len(C)]}\n\n{'[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'}"
        finaltext = Q('<code>$ </code><code>'+FIX(C)+'</code>\n'+M(FIX(o)) if o else f'$ {M(FIX(C))}')

        if id == str(MY_USER_ID): await E.edit(finaltext,parse_mode="HTML")
        else: await E.reply(finaltext,parse_mode="HTML")
    elif E.sender_id == MY_USER_ID:
        if Shell_ON_T:
            Shell_ON_T = False
            await E.edit("<code>SHELL</code>\n\nON\nOFF", parse_mode='HTML')
            await asyncio.sleep(0.3)
            await E.edit("<code>SHELL</code>\n\nON\n<blockquote>OFF</blockquote>", parse_mode="HTML")
        else:
            Shell_ON_T = True
            await E.edit("<code>SHELL</code>\n\nON\nOFF", parse_mode="HTML")
            await asyncio.sleep(0.3)
            await E.edit("<code>SHELL</code>\n\n<blockquote>ON</blockquote>\nOFF", parse_mode='HTML')
        await asyncio.sleep(5)
        await E.delete()
    else:
        if Shell_ON_T:
            Shell_ON_T = False
            shell_t = await E.reply("ON\n<blockquote>OFF</blockquote>", parse_mode="HTML")
        else:
            Shell_ON_T = True
            shell_t = await E.reply("<blockquote>ON</blockquote>\nOFF", parse_mode='HTML')
        await asyncio.sleep(5)
        await shell_t.delete()
        await E.delete()