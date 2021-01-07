import discord
from discord.ext import commands
from datetime import datetime
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv() # Load variables from the .env file

# Bot info
bot_token = os.getenv("BOT_TOKEN")
command_prefix = os.getenv("COMMAND_PREFIX")

# Bot customization
bot_color = 16225050
bot_footer_text = "Crypto Price Bot | By Kean#9123"
bot_footer_icon = "https://i.imgur.com/UY53jZM.png"

client = commands.Bot(command_prefix=command_prefix)

@client.event
async def on_ready():
    print("Ready.")

# Start the bot
client.run(bot_token)