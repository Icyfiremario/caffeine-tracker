import os

import discord
from dotenv import load_dotenv
from user import User

users = {}

def main():
    global users
    load_dotenv()
    BOT_KEY = os.getenv('DISCORD_KEY')

    intent = discord.Intents.default()
    intent.message_content = True
    intent.messages = True

    client = discord.Client(intents=intent)

    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.author not in users.keys():
            users[message.author] = User()

        user = users[message.author]

        if message.content.startswith('!add dose'):
            args = message.content.split("!add dose ")

            if len(args) > 1:
                user.add_dose(float(args[1]))
                await message.channel.send(f"Adding dose of {args[1]} mg")
            else:
                await message.channel.send("Please specify the amount of caffeine to add in milligrams")

        if message.content.startswith("!check"):
            user.check_caffeine()
            await message.channel.send(f"Your current caffeine level is {user.check_caffeine()} mg")

    client.run(BOT_KEY)

    return

if __name__ == "__main__":
    main()