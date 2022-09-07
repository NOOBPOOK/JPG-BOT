import nextcord
from nextcord.ui import Button, View, Select
from nextcord.utils import get
from nextcord.ext import commands
import os
import pytesseract as tess
from PIL import Image
import requests
import shutil

intents = nextcord.Intents(messages=True, message_content=True, guilds=True, voice_states=True, members=True)
client = commands.Bot(command_prefix="#", help_command=None, intents=intents)

#image manipulation
@client.command()
async def capture(ctx):
    image_url = ctx.message.attachments[0].url
    with open('manipulation','wb') as f:
        image = requests.get(image_url, stream = True)
        image.raw.decode_content = True
        shutil.copyfileobj(image.raw, f)            
    image = Image.open('manipulation')
    text = tess.image_to_string(image)
    await ctx.reply(text)
    
client.run("******BOT-TOKEN*******")
