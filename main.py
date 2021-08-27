import discord
import os
import random

from config import TOKEN

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game("Fortnite"))
    print('We have logged in as {0.user}'.format(client))


# generate random percentage and relevant loading bar
def get_percentage():
    perc = random.randint(0,100)

    if perc == 0:
        bar = '░░░░░░░░░░'
    elif perc in range(1,10):
        bar = '█░░░░░░░░░'
    elif perc in range(10,20):
        bar = '██░░░░░░░░'
    elif perc in range(20,30):
        bar = '███░░░░░░░'
    elif perc in range(30,40):
        bar = '████░░░░░░'
    elif perc in range(40,50):
        bar = '█████░░░░░'
    elif perc in range(50,60):
        bar = '██████░░░░'
    elif perc in range(60,70):
        bar = '███████░░░'
    elif perc in range(70,80):
        bar = '████████░░'
    elif perc in range(80,90):
        bar = '█████████░'
    elif perc in range(90,100):
        bar = '██████████'
    
    print(f'{perc} and {bar}')
    return(f'Egg\'s stink level is {perc}% {bar}')


# event that listens for messages
@client.event
async def on_message(message):

    # print every message to console
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # prevent bot from monitoring its own messages and therefore getting stuck in an infinite loop
    if message.author == client.user:
        return

    # basic stinks response
    if user_message.lower() == 'egg':
        await message.channel.send('stinks')
        return
    
    # percentage
    if message.content.startswith('$eggstinks'):
        await message.channel.send(str(get_percentage()))
        return

    
            

client.run(TOKEN)