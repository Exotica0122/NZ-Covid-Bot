import discord
import os
import requests
import json

from keep_alive import keep_alive
from covid import get_covid_info

covid_image_url = "https://www.clevelandclinic.org/healthinfo/ShowImage.ashx?PIC=4480"

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$covid"):
      covid_info = get_covid_info()
      embedVar = discord.Embed(title="NZ Covid Cases", color=0x00ff00)
      embedVar.set_thumbnail(url=covid_image_url)
      embedVar.add_field(name="Current Confirmed Cases", value=covid_info["confirmed"], inline=False)
      embedVar.add_field(name="Current Deaths", value=covid_info["deaths"], inline=False)
      embedVar.add_field(name="New Confirmed Cases", value=covid_info["confirmed_daily"], inline=False)
      embedVar.add_field(name="Date", value=covid_info["date"], inline=False)
      await message.channel.send(embed=embedVar)

    if msg.startswith("$new"):
      await message.channel.send(MOH_covid_info()) 

keep_alive()
client.run(os.environ['token'])
