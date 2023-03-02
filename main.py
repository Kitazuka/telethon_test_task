import asyncio
import os

from telethon import TelegramClient
from dotenv import load_dotenv


load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")
SESSION_NAME = os.getenv("SESSION_NAME")
MESSAGE = "Some message that i need to send"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def main():
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        await client.sign_in(PHONE, input("Enter the code: "))

    with open("Groups.txt", "r") as f:
        groups = f.readlines()

    for group in groups:
        try:
            await client.send_message(group, MESSAGE)
        except Exception as e:
            print(f"Error sending message to group {group}: {e}")
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
