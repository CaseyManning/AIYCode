import discord
import asyncio

client = discord.Client()

channel = None

def send_image(filename):
    if not channel is None:
        client.send_file(channel, filename)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!enable'):
        channel = message.channel
        await client.send_message(message.channel, 'Enabling camera...')
    elif message.content.startswith('!disable'):
        channel = None
        await client.send_message(message.channel, 'Disabling camera...')

client.run('NDY1NjQ5ODkyNzY1NzI4Nzc4.DiuiSg.sbOP4SJbOaszX9qmqr6FTxgmytU')
