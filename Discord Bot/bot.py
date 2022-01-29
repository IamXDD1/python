import discord
import os
import py_dotenv
from firebase import *
from textFile import *

client = discord.Client()

py_dotenv.read_dotenv('.env')

TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$intro':
        await message.author.send(INTRO)

@client.event
async def on_connect():
    print('Your Teaching Assistant is Online!')

client.run(TOKEN)