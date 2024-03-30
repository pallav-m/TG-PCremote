from telethon import events
from telethon.sync import TelegramClient

import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

from decouple import config

api_id = config('api_id')
api_hash = config('api_hash')
authorised_user_id = config('authorised_user_id')

# setting up telegram client
client: TelegramClient = TelegramClient('bot', api_id, api_hash)


@client.on(events.NewMessage())
async def ping_handler(event):
    message = event.message.message
    message_id = event.message.from_id

    logging.info(f"Received message: {message} from id: {message_id}")

    if message_id.user_id == authorised_user_id:
        logging.info(f"Message came from authorised user. Running commands.")

    else:
        await client.send_message(message_id.user_id, "You are not authorised.")
        logging.info(f"Unauthorised user: {message_id}")



logging.info("starting responder")
with client:
    client.run_until_disconnected()
