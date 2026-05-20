import os
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ID, GIS, GS
import wikipediaapi

MY_USER_ID = os.getenv("MY_USER_ID")


@SPY(outgoing=True, pattern=r"^!!wiki (.*)")
async def wiki(E):
    """For .google command, fetch content from wikipediaapi."""
    id = str(ID(E))
    if id not in GS() and id not in GIS() and id != MY_USER_ID:
        return
    replied = await E.get_reply_message()
    match = E.pattern_match.group(1)
    wiki = wikipediaapi.AsyncWikipedia(
        user_agent="MyProjectName (merlin@example.com)", language="en"
    )
    page = wiki.page(match)
    if not await page.exists():
        if id == MY_USER_ID:
            await E.edit("Page not found.")
        else:
            if replied:
                await replied.reply("Page not found.")
            else:
                await E.reply("Page not found.")
        return
    result = await page.summary
    if len(result) >= 4000:
        file = open("output.txt", "w+")
        file.write(result)
        file.close()
        await E.client.send_file(
            E.chat_id,
            "output.txt",
            reply_to=E.id,
            caption="`Output too large, send as file.`",
        )
        if id == MY_USER_ID:
            await E.delete()
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        return
    if id == MY_USER_ID:
        await E.edit(
            "<b>Search:</b>\n<blockquote><code>"
            + match
            + "</code></blockquote>\n\n<b>Result:</b>\n<blockquote>"
            + result
            + "</blockquote>",
            parse_mode="html",
        )
    elif replied:
        await replied.reply(
            "<b>Search:</b>\n<blockquote><code>"
            + match
            + "</code></blockquote>\n\n<b>Result:</b>\n<blockquote>"
            + result
            + "</blockquote>",
            parse_mode="html",
        )
    else:
        await E.reply(
            "<b>Search:</b>\n<blockquote><code>"
            + match
            + "</code></blockquote>\n\n<b>Result:</b>\n<blockquote>"
            + result
            + "</blockquote>",
            parse_mode="html",
        )
