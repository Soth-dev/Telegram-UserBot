from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ID, GIS, GS, M, Q
from PIL import Image, ImageDraw, ImageFont
import os

MY_USER_ID = os.getenv("MY_USER_ID")


@SPY(pattern="(?s)^!!write ?(.*)?")
async def writer(E: NewMessage.Event):
    id = str(ID(E))
    if id not in GS() and id not in GIS() and id != MY_USER_ID:
        return
    if E.pattern_match and E.pattern_match.group(1):
        text = E.text.split(maxsplit=1)[1]
    elif E.is_reply:
        text = (
            E.reply_to.quote_text
            if E.reply_to.quote
            else (await E.get_reply_message()).text
        )
        if not text:
            return
    else:
        return  # await E.edit("error")
    if id == MY_USER_ID:
        await E.edit(Q(M("Writing...")), parse_mode="HTML")
    img = Image.open("tgubot/assets/images/note.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("tgubot/assets/fonts/ass.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    bbox = font.getbbox("hg")
    line_height = bbox[3] - bbox[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height + 4
    file = ".cache/note.jpg"
    img.save(file)
    if E.is_reply:
        rmsg = await E.get_reply_message()
        await rmsg.reply(file=file)
    else:
        await E.reply(file=file)
    os.remove(file)
    await E.delete()


def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = len(line) // 55
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:24]
