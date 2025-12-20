from telethon import TelegramClient
from prettytable import PrettyTable

api_id = 11111111
api_hash = "c2a.......5ac"
phone = "+380996506061"

client = TelegramClient("lab1_session", api_id, api_hash)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input("Enter Telegram login code: ")
        await client.sign_in(phone=phone, code=code)

    chat_link = "https://t.me/+IaPpmAJ_sw8yZDVi"
    chat = await client.get_entity(chat_link)
    users = await client.get_participants(chat)

    print(f"\n=== Group name: {chat.title} ===\n")

    table = PrettyTable(["ID", "First name", "Last name"])

    for user in users:
        table.add_row([user.id, user.first_name, user.last_name])

    print(table)

    await client.send_message("@minonskyy", "test test test ")
    print("\nMessage sent!")

with client:
    client.loop.run_until_complete(main())
