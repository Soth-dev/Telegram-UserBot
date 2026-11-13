from telethon.events import NewMessage
from telethon.tl.custom.participantpermissions import ParticipantPermissions
from telethon.tl.types import InputMediaPoll, Poll, PollAnswer, TextWithEntities
import random
from tgubot.handler.spy import SPY


@SPY()
async def ok(E: NewMessage.Event):
    if E.sender_id in [7466863227]:
        # print(E)
        e = await E.client.get_entity(E.chat)
        p = await E.client.get_permissions(e, "me")
        print(e, "\n\n", dir(p), "\n\n\n\n")
        match p:
            # 2. Permanently muted / no text send rights (global mute, personal mute, or broadcast channel)
            case ParticipantPermissions(send_messages=True):
                await E.reply("Ok.")

            # 3. Can send text, but media/files are disabled
            case ParticipantPermissions(send_media=True):
                await E.client.send_file(
                    E.chat_id,
                    "/storage/emulated/0/Download/ub/IMG_20261108_104908_286.jpg",
                    reply_to=E.id,
                )

            # 4. Can send text/media, but stickers, GIFs, links, or polls are disabled
            # case ParticipantPermissions(send_stickers=False):
            #     print("Restricted: send_stickers is False")

            # case ParticipantPermissions(send_gifs=False):
            #     print("Restricted: send_gifs is False")

            case ParticipantPermissions(send_polls=True):
                poll = InputMediaPoll(
                    poll=Poll(
                        id=0,  # Telethon/Telegram assigns the actual ID automatically
                        hash=0,
                        question=TextWithEntities(text="Ok.", entities=[]),
                        answers=[
                            PollAnswer(
                                text=TextWithEntities(text="Ok.", entities=[]),
                                option=str(i).encode(),
                            )
                            for i in range(random.randint(1, 6))
                        ],
                        public_voters=True,  # False for anonymous poll (default in groups)
                        multiple_choice=True,  # True to allow picking multiple answers
                        quiz=False,  # True for quiz mode
                    )
                )

                await E.client.send_file(
                    E.chat_id, file=poll, reply_to=E.reply_to_msg_id or E.id
                )
