import discord
import os
from dotenv import load_dotenv
load_dotenv() # Load variables from the .env file

bot_token = os.getenv("BOT_TOKEN")
command_prefix = os.getenv("COMMAND_PREFIX")

client = discord.Client(command_prefix=command_prefix)

@client.event
async def on_ready():
    print("Ready.")

# Start the bot
client.run(bot_token)