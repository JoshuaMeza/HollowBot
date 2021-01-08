"""
Author Joshua Meza
Date 06/01/2021
Version 1.0.0
Wins Module
"""
import discord
from discord.ext import commands
import random
from modules.Connector import *


class Wins(commands.Cog):
    def __init__(self, client):
        """
        This is a constructor
        """
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Victories module loaded!')

    # Commands
    @commands.command(aliases=['WINS', 'score', 'SCORE'])
    async def wins(self, ctx):
        """
        This method manages the wins command
        Args:
            self (object): The object itself
            ctx (object): Context
            c (object): Connector object
        Returns:
            Nothing
        """
        if (ctx.channel.name == 'playground'):
            score = -1

            try:
                c = Connector()
                score = c.getWins(str(ctx.author.id))
            except Exception as e:
                score = -1

            if (score != -1):
                if (score == 1):
                    await ctx.send('<@{}> has {} win!'.format(str(ctx.author.id), str(score)))
                else:
                    await ctx.send('<@{}> has {} wins!'.format(str(ctx.author.id), str(score)))
            else:
                embed = discord.Embed(
                    title='Oops!',
                    description='Sorry, but I can\'t tell you your high score, I think I lost my Legends Journal...',
                    colour=discord.Colour.red()
                )
                await ctx.send(embed=embed, delete_after=10.0)

            return


def setup(client):
    client.add_cog(Wins(client))
