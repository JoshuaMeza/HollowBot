"""
Author Joshua Meza
Date 01/01/2021
Version 1.0.2
A bot which plays with you! It can also store wins amount.
"""
import discord
from discord.ext import commands
import os
import sys
import random
from dotenv import load_dotenv
from keepAlive import *

# Key words tuple
words = (
    'bored',
    'play',
    'game'
)
# Reactions dictionary
reactions = {
    1: '✨',
    2: '🔥',
    3: '👀',
    4: '🕶️',
    5: '🙋'
}

# Commands extension initializer
client = commands.Bot(command_prefix='--')

client.remove_command("help")

# Load extensions
# NOTE: Run in TERMINAL in the code directory or it wont work!
# cd code/          python3 main.py
for filename in os.listdir('modules/'):
    if (filename.endswith('.py') and filename != 'Connector.py'):
        client.load_extension('modules.{}'.format(filename[:-3]))


# Events


@client.event
async def on_ready():
    """
    When the bot gets activated, this function prints a message
    """
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """
    This function activates when someone sent a message
    Args:
        message (object): Message sent in chat
        msg (object): "Let's play!" message
        reactions (dict): Reactions for suggestion messages
        client (object): 
    Returns:
        Nothing
    """
    # Bot sending a message
    if message.author == client.user:
        return

    # Checkes if someone in the server wants to play
    elif (not message.content.startswith('--') and any(word in message.content for word in words)):

        await message.add_reaction(reactions[random.randint(1, len(reactions))])

        if (message.channel.name == 'playground'):
            await message.channel.send('Hey <@{}>! If you want I can play with you my friend! :)\nJust say "--play".'.format(str(message.author.id)))
        else:
            await message.channel.send('Hey <@{}>! If you want I can play with you my friend! :)\nJust follow me to the channel called "playground" and say "--play".'.format(str(message.author.id)))

        return

    await client.process_commands(message)


@client.event
async def on_command_error(ctx, error):
    """
    This function sends a temporal message if a user tries to use an unknown command
    Args:
        ctx (object): Context
        error (object): Error found
    Returns:
        Nothing
    """
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title='Oops!',
            description='Sorry, but I don\'t know what you are trying to do...\n \
                If you want, you can check my commands with "--info".',
            colour=discord.Colour.red()
        )
        await ctx.send(embed=embed, delete_after=10.0)

# Activate web host
keep_alive()

# Activate bot
load_dotenv()
client.run(os.getenv('TOKEN'))
