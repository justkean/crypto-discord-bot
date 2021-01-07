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
bot_error_color = 15549239
bot_footer_text = "Crypto Price Bot | By Kean#9123"
bot_footer_icon = "https://i.imgur.com/UY53jZM.png"

# API base link - Documentation: https://www.coingecko.com/en/api
api_base = "https://api.coingecko.com/api/v3/simple/price?ids="

# Currency information
currency_name = "USD"
currency_symbol = "$"

client = commands.Bot(command_prefix=command_prefix)

# To be used whenever there is an error within the bot
async def send_error_embed(ctx, message):
    embed = discord.Embed(title="Error", description="An error occured whilst trying to process your last action. You can find more information about the error below.", timestamp=datetime.utcnow(), color=bot_error_color)
    embed.add_field(name="Message", value=f"```{message}```")
    embed.set_footer(text=bot_footer_text, icon_url=bot_footer_icon)
    await ctx.channel.send(embed=embed)

@client.event
async def on_ready():
    print("Ready.")

@client.command()
async def prices(ctx):
    response = requests.get(f"{api_base}bitcoin-cash,monero,ripple,ethereum,litecoin,bitcoin&vs_currencies={currency_name.lower()}") # Get all available coin IDs from: https://api.coingecko.com/api/v3/coins/list

    # If request wasn't successful, send error embed
    if (response.status_code != 200):
        await send_error_embed(ctx, "Failed to fetch the latest cryptocurrency prices. Please try again later.")
        return

    # Load response as JSON
    respJSON = json.loads(response.text)

    embed = discord.Embed(title="Current crypto prices", description="Below are the prices of some of the most popular cryptocurrencies.", timestamp=datetime.utcnow(), color=bot_color)

    # Add each coin from the response as a field in the final embed
    for coin in respJSON:
        coinName = coin.capitalize().replace("-", " ") # This will turn e.g. "bitcoin-cash" into "Bitcoin cash"
        coinValue = respJSON[coin]['usd']

        embed.add_field(name=coinName, value=f"```{currency_symbol}{coinValue} {currency_name}```", inline=True)

    embed.set_footer(text=bot_footer_text, icon_url=bot_footer_icon)
    await ctx.channel.send(embed=embed)

# Start the bot
client.run(bot_token)