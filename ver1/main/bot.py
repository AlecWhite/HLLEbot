# bot.py
import os
import random
from dotenv import load_dotenv

#lib magica para bots
from discord.ext import commands
#web scrapper lib
from bs4 import BeautifulSoup

import requests
import regex
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#url del serb
url = "https://www.battlemetrics.com/servers/hll/6822841"
#request to downlaod the whole html request
page = requests.get(url)


#funciona un pelin asi-asi con caracteres especiales
#tendria que mirarlo en un futuro
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='ping')
async def ping_y_pong(ctx):
    response = "pong"
    await ctx.send(response)


@bot.command(name='jugadores')
async def jugadores(ctx):
    print("jugadores called")
    # use the web scrapper to parse the html into a beautifulsoup object
    soup = BeautifulSoup(page.content, 'html.parser')
    #regex magic incantation
    pattern = '<dd>([0-9]|[1-8][0-9]|9[0-9]|100)/100</dd>'
    #converted to string because I think it works better with regex
    results = str(soup.find(id='serverPage'))
    print(results)
    re = str(regex.findall(pattern, results))

    print(re)
    response = "Hay actualmente: " + re.strip('['']') + " jugandores online."
    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



bot.run(TOKEN)