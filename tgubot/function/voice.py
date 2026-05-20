import os
import asyncio
from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import Q, M, B

msg_for_percentage = NewMessage.Event


async def callback(current, total):
    global msg_for_percentage
    percent = round(current / total * 100, 2)
    await msg_for_percentage.edit(
        Q(f"Uploaded {M(current)} out of {M(total)} bytes: {M(str(percent) + '%')}"),
        parse_mode="HTML",
    )
    await asyncio.sleep(3)


@SPY(outgoing=True, pattern=r"^!!voice$")
async def vc(E: NewMessage.Event):
    global msg_for_percentage
    msg_for_percentage = E
    message = await E.get_reply_message()
    if message.audio or message.voice:
        file = message.audio or message.voice
        await E.edit(Q(B("Downloading...")), parse_mode="HTML")
        file = await E.client.download_file(file, "voice.mp3")
        await E.edit(Q(M("Sending...")), parse_mode="HTML")
        await E.client.send_file(
            E.chat_id,
            "voice.mp3",
            reply_to=message,
            voice_note=True,
            progress_callback=callback,
        )
        os.remove("voice.mp3")
        await asyncio.sleep(3)
        await E.delete()
    else:
        await E.edit("**Bot doesn't support magic! Use audio or voice message!**")
