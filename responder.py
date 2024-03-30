from telethon import events
from telethon.sync import TelegramClient

import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

from decouple import config

api_id = config('api_id')
api_hash = config('api_hash')
authorised_user = config('authorised_username')

# setting up telegram client
client: TelegramClient = TelegramClient('bot', api_id, api_hash)


@client.on(events.NewMessage(incoming=True))
async def ping_handler(event):
    message = event.message.message
    message_id = event.message.from_id
    sender = await event.get_sender()

    logging.info(f"Received message: {message} from id: {message_id.user_id}")
    logging.info(sender.username)

    if (sender.username == authorised_user):
        logging.info(f"Message came from authorised user. Running commands.")


    else:
        await client.send_message(sender, "You are not authorised.")
        logging.info(f"Unauthorised user: {message_id}")


logging.info("starting responder")

client.start()
client.run_until_disconnected()
