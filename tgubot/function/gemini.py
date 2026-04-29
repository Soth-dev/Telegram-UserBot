from google import genai
from google.genai.types import GenerateContentConfig
from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ARG, Q, M, GR, T


client = genai.Client()


@SPY(outgoing=True, pattern="(?s)^!!ai (.+)")
async def gemini(E: NewMessage.Event):
    L = await E.reply(Q(M("Generating...")), parse_mode="HTML")
    r = gen_resp(ARG(E, 1), T(await GR(E)))
    await L.edit(r)


def gen_resp(text: str, reply: str | None = None) -> str:
    config = GenerateContentConfig(system_instruction=reply)
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=text, config=config
    )
    return response.text if response.text else "."
