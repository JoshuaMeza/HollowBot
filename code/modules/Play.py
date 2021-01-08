"""
Author Joshua Meza
Date 06/01/2021
Version 1.0.0
Play Module
"""
import discord
from discord.ext import commands
import random
from modules.Connector import *


class Play(commands.Cog):
    def __init__(self, client):
        """
        This is a constructor
        """
        self.client = client
        self.reactions = {
            1: '👊',
            2: '✋',
            3: '✌️'
        }

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Play module loaded!')

    # Commands
    @commands.command(aliases=['PLAY'])
    async def play(self, ctx):
        """
        This method manages the play command
        Args:
            self (object): The object itself
            ctx (object): Context
            reactions (dict): Reactions for the game 
            msg (object): 'Let's play' message
            selected (str): Reaction selected
            reaction (object): Reaction made
            user (object): Last user who made a reaction
            flagDoSave (bool): Flag which activates saving process
            c (object): Connector object
            embed (object): A Discord message type
        Returns:
            Nothing
        """
        if (ctx.channel.name == 'playground'):
            msg = await ctx.send('Lets play!')

            for reaction in self.reactions.values():
                await msg.add_reaction(reaction)

            selected = self.reactions[random.randint(1, len(self.reactions))]

            def check(reaction, user):
                """
                This method checks if the reaction is from the user who wanted to play
                Ars:
                    reaction (object): Reaction made
                    user (object): Last user who made a reaction
                Returns:
                    True if it is the user, False if not
                """
                return user == ctx.author

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=10.0, check=check)
            except Exception as e:
                await msg.delete()
                await ctx.send('Time out! You need to decide faster <@{}>.'.format(str(ctx.author.id)))
            else:
                flagDoSave = False
                await ctx.send(selected)
                if (reaction.emoji == self.reactions[1]):
                    if (selected == reaction.emoji):
                        result = 'Tie!'
                    elif (selected == self.reactions[2]):
                        result = 'I won!'
                    else:
                        result = 'You won!'
                        flagDoSave = True
                elif (reaction.emoji == self.reactions[2]):
                    if (selected == reaction.emoji):
                        result = 'Tie!'
                    elif (selected == self.reactions[3]):
                        result = 'I won!'
                    else:
                        result = 'You won!'
                        flagDoSave = True
                else:
                    if (selected == reaction.emoji):
                        result = 'Tie!'
                    elif (selected == self.reactions[1]):
                        result = 'I won!'
                    else:
                        result = 'You won!'
                        flagDoSave = True

                await ctx.send(result)

                if (flagDoSave):
                    try:
                        c = Connector()
                        c.updateScore(str(ctx.author.id))
                    except Exception as e:
                        embed = discord.Embed(
                            title='Oops!',
                            description='Sorry, but I can\'t save your victory in my Legends Journal, I think I lost my pen...',
                            colour=discord.Colour.red()
                        )
                        await ctx.send(embed=embed, delete_after=10.0)


def setup(client):
    client.add_cog(Play(client))
