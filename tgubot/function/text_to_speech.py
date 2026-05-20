import asyncio
import os
from telethon.events import NewMessage
from gtts import gTTS
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import M, Q


@SPY(outgoing=True, pattern="^!!tts")
async def tts(E: NewMessage.Event):
    message = E.message
    args = E.text.split()[1:]
    delmsg = ""

    if message.is_reply:
        delmsg = await message.get_reply_message()
        delmsg = delmsg.text

    if args:
        delmsg = " ".join(args).lower()

    if delmsg:
        await E.edit(Q(M(f"TTS: {delmsg}")), parse_mode="HTML")
        filename = ".cache/voicetts.mp3"

        tts = gTTS(delmsg)
        tts.save(filename)

        reply_msg = await E.get_reply_message()
        if reply_msg:
            await E.client.send_file(
                E.chat_id, filename, voice_note=True, reply_to=reply_msg.id
            )
        else:
            await E.client.send_file(
                E.chat_id, filename, voice_note=True, reply_to=E.id
            )
        os.remove(filename)
        await asyncio.sleep(1)
        await E.delete()
    else:
        await E.delete()
