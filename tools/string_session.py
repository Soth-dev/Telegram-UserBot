from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")

api_id = getenv("API_KEY")
api_hash = getenv("API_HASH")

if not all([api_id, api_hash]):
    print("please add the env in .env")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    ...  # use the client

    # Save the string session as a string; you should decide how
    # you want to save this information (over a socket, remote
    # database, print it and then paste the string in the code,
    # etc.); the advantage is that you don't need to save it
    # on the current disk as a separate file, and can be reused
    # anywhere else once you log in.
    string = client.session.save()
    print(f"\n{string}\n")

# Note that it's also possible to save any other session type
# as a string by using ``StringSession.save(session_instance)``:

# client = TelegramClient('sqlite-session', api_id, api_hash)
# string = StringSession.save(client.session)
