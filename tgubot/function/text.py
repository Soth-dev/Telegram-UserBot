import string
import unicodedata
import asyncio

from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ERR

# Define dual character. Make sure that mapping is bijective.
FLIP_RANGES = [
    (string.ascii_lowercase, "ɐqɔpǝɟƃɥᴉɾʞꞁɯuodbɹsʇnʌʍxʎz"),
    # alternatives: l:ʅ
    (string.ascii_uppercase, "ⱯᗺƆᗡƎᖵ⅁HIᒋ⋊ꞀWNOԀꝹᴚS⊥∩ɅMX⅄Z"),
    # alternatives: L:ᒣ⅂, J:ſ, F:߃Ⅎ, A:∀ᗄ, U:Ⴖ, W:Ϻ, C:ϽↃ, Q:Ό, M:Ɯꟽ
    (string.digits, "0ІᘔƐᔭ59Ɫ86"),
    (string.punctuation, "¡„#$%⅋,)(*+'-˙/:؛>=<¿@]\\[ᵥ‾`}|{~"),
]

UNICODE_COMBINING_DIACRITICS = {
    "̈": "̤",
    "̊": "̥",
    "́": "̗",
    "̀": "̖",
    "̇": "̣",
    "̃": "̰",
    "̄": "̱",
    "̂": "̬",
    "̆": "̯",
    "̌": "̭",
    "̑": "̮",
    "̍": "̩",
}

TRANSLITERATIONS = {"ß": "ss"}

# character lookup
_CHARLOOKUP = {}
for chars, flipped in FLIP_RANGES:
    _CHARLOOKUP.update(zip(chars, flipped))

# get reverse direction
for char in _CHARLOOKUP.copy():
    # make 1:1 back transformation possible
    assert (
        _CHARLOOKUP[char] not in _CHARLOOKUP or _CHARLOOKUP[_CHARLOOKUP[char]] == char
    ), "%s has ambiguous mapping" % _CHARLOOKUP[char]
    _CHARLOOKUP[_CHARLOOKUP[char]] = char

# lookup for diacritical marks, reverse first
_DIACRITICSLOOKUP = dict(
    [
        (UNICODE_COMBINING_DIACRITICS[char], char)
        for char in UNICODE_COMBINING_DIACRITICS
    ]
)
_DIACRITICSLOOKUP.update(UNICODE_COMBINING_DIACRITICS)


def transform(text, transliterations=None):
    transliterations = transliterations or TRANSLITERATIONS

    for character in transliterations:
        text = text.replace(character, transliterations[character])

    input_chars = list(text)
    input_chars.reverse()

    output = []
    for character in input_chars:
        if character in _CHARLOOKUP:
            output.append(_CHARLOOKUP[character])
        else:
            char_normalized = unicodedata.normalize("NFD", character)

            for c in char_normalized[:]:
                if c in _CHARLOOKUP:
                    char_normalized = char_normalized.replace(c, _CHARLOOKUP[c])
                elif c in _DIACRITICSLOOKUP:
                    char_normalized = char_normalized.replace(c, _DIACRITICSLOOKUP[c])

            output.append(unicodedata.normalize("NFC", char_normalized))

    return "".join(output)


@SPY(outgoing=True, pattern=r"^!!flip(\s+[\S\s]+|$)")
async def flip_message(E: NewMessage.Event):
    reply_message = await E.get_reply_message()
    text = (
        reply_message.text
        if reply_message and not (E.pattern_match and E.pattern_match.group(1))
        else E.pattern_match.group(1)
        if E.pattern_match
        else ""
    )
    flipped = transform(text)
    await E.edit(flipped)


@SPY(outgoing=True, pattern="(?s)!!type ?(.+)?")
async def typeerr(E: NewMessage.Event):
    try:
        reply_msg = await E.get_reply_message()
        final_text = E.pattern_match.group(1) if E.pattern_match else ""
        if reply_msg and not final_text:
            final_text = reply_msg.text
        elif not reply_msg and not final_text:
            return
        i = ""
        await E.edit("|")
        await asyncio.sleep(0.2)
        for j in final_text:
            await asyncio.sleep(0.05)
            await E.edit(i + j + "|")
            i += j
            await asyncio.sleep(0.3)
        await E.edit(i)
        # await E.edit(i)
    except Exception:
        print(ERR())
