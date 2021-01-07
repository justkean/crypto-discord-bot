import discord
import os
from dotenv import load_dotenv
load_dotenv() # Load variables from the .env file

BOT_TOKEN = os.getenv('BOT_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')

client = discord.Client(command_prefix=COMMAND_PREFIX)

@client.event
async def on_ready():
    print('Ready.')

# Start the bot
client.run(BOT_TOKEN)