import discord
import asyncio
import _thread

client = discord.Client()

channel = None

def send_image(filename):
    global channel
    if channel is not None:
        print('Sending image...')
        client.send_message(channel, 'Detected a face')
        client.send_file(channel, filename)
    else:
        print('Channel is None... have you enabled the bot?')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global channel
    if message.content.startswith('!enable'):
        channel = message.channel
        await client.send_message(channel, 'Enabling camera...')
    elif message.content.startswith('!disable'):
        channel = None
        await client.send_message(channel, 'Disabling camera...')

_thread.start_new_thread(client.run, ('NDY1NjQ5ODkyNzY1NzI4Nzc4.DiuiSg.sbOP4SJbOaszX9qmqr6FTxgmytU',))
