"""
Author Joshua Meza
Date 06/01/2021
Version 1.0.0
Information Module
"""
import discord
from discord.ext import commands
import random


class Info(commands.Cog):
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
        print('Information module loaded!')

    # Commands
    @commands.command(aliases=['INFO', 'help', 'HELP'])
    async def info(self, ctx):
        """
        This method manages the information command
        Args:
            self (object): The object itself
            ctx (object): Context
            embed (object): A Discord message type
        Returns:
            Nothing
        """
        embed = discord.Embed(
            title='More about me!',
            description='I\'m a bot which loves to play "rock paper scissors", do you want to play with me?',
            colour=discord.Colour.red()
        )

        embed.add_field(name='Playground',
                        value='All commands (except for "--info") can only be executed in a channel that has the name "playground".',
                        inline=False)
        embed.add_field(name='Commands',
                        value='**--play**\tThis command starts a new game between us.\n**--wins**\tThis command lets me know if you want to know your amount of victories!\n**--info**\tThis command helps you to know more about me.',
                        inline=False)
        embed.add_field(name='Documentation',
                        value='You can learn a lot more about me here: https://github.com/JoshuaMeza/HollowBot',
                        inline=False)
        embed.add_field(name='Icon',
                        value='My icon is from yuilero, go and send her some love: https://www.instagram.com/p/CHiU20dF16C/?utm_source=ig_web_copy_link',
                        inline=False)
        embed.set_image(url='https://instagram.fcjs3-2.fna.fbcdn.net/v/t51.2885-15/e35/124418912_812561622859381_5253393339216761283_n.jpg?_nc_ht=instagram.fcjs3-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=1VnfDlHZf8EAX_3ywrm&tp=1&oh=96529d233a744f6c482149cd504bd18b&oe=60199C5A')
        embed.set_footer(text='#stayhome #keeplearning #fun')

        await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))
