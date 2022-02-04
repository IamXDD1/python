import discord
#from discord.ext import commands
import os
import py_dotenv
import json
from firebase import *

with open('setting.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

#bot = commands.Bot(command_prefix='@')

client = discord.Client()

py_dotenv.read_dotenv('.env')

TOKEN = os.getenv('TOKEN')

def FirstCheck(author):
    state = 0

    if checkIDexist(author):
        dic_author = doc_ref(col='Clients', doc=author).get().to_dict()
        state = dic_author['state']
    else:
        doc_ref(col='Clients', doc=author).set({'state': int(state),
                                                'loggedIn': False,
                                                'lastUse': getCurrTime(),
                                                'SignedUp': False})

    dic_author = doc_ref(col='Clients', doc=author).get().to_dict()

    if dic_author['loggedIn']:
        if checkLoggedInExpire(author):
            doc_ref(col='Clients', doc=author).update({'loggedIn': False})
        else:
            doc_ref(col='Clients', doc=author).update({'loggedIn': True})

    return state, dic_author

def Update(state, author):
    doc_ref(col='Clients', doc=author).update({'state': int(state), 'lastUse': getCurrTime()})

def fn_Embed():
    embed = discord.Embed(
        title='Intro',
        description='Hello, I am a Takodachi to manage the server!',
        colour=discord.Colour.purple()
    )

    embed.set_footer(text='number-3584')
    embed.set_image(
        url='https://preview.redd.it/3e6zphwn0bt71.gif?format=png8&s=14086780fc21f77923c3f6bd3d797da8732331d9')
    embed.set_thumbnail(
        url='https://preview.redd.it/3e6zphwn0bt71.gif?format=png8&s=14086780fc21f77923c3f6bd3d797da8732331d9')
    embed.set_author(name='XDD#3584',
                     icon_url='https://preview.redd.it/3e6zphwn0bt71.gif?format=png8&s=14086780fc21f77923c3f6bd3d797da8732331d9')
    embed.add_field(name='Commands', value='/intro\n/help', inline=False)
    embed.add_field(name='Field 2', value='value 2', inline=True)
    embed.add_field(name='Field 3', value='value 3', inline=True)
    return embed

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/intro') or message.content == '/help':
        author = str(message.author)
        state, dic_author = FirstCheck(author)

        await message.author.send(embed=fn_Embed())
        Update(state, author)

@client.event
async def on_connect():
    print('>> Your Test Bot is Online! <<')

@client.event
async def on_member_join(member):
    #channel = bot.get_channel(~~~)
    #await channel.send
    await message.channel.send(f"{member} join!")
    await message.author.send(embed=fn_Embed())

@client.event
async def on_member_leave(member):
    await message.channel.send(f"{member} leave...")
    await message.author.send('See you next time~')

#@bot.command()
#async def ping(ctx):
#    await ctx.send(bot.latency)

client.run(TOKEN)