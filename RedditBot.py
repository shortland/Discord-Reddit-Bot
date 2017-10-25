import discord
import asyncio
import os
import subprocess

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Results from Reddit.com'))

@client.event
async def on_message(message):
    if message.content.startswith("~r"):
        stuff = message.content
        stuff = stuff.replace("~r ", "", 1)
        stuff = stuff.replace(" ", "\ ")
        await client.send_typing(message.channel)
        from subprocess import call
        result = subprocess.run(["perl", "reddit_main.pl", "%s" % stuff], stdout=subprocess.PIPE)
        datas = result.stdout.decode("utf-8")
        await client.send_message(message.channel,"%s" % datas)

client.run('')