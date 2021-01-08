# HollowBot - Beginners Tutorial and Documentation

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/Cover.png" width="100%">

> The icon is from [yuilero](https://www.instagram.com/yuilero/).

Welcome to HollowBot's repository! Here you can find everything about the bot and some steps to start building your own. Enjoy!

## Index

- [Description](https://github.com/JoshuaMeza/HollowBot#description)
- [Add it into your Discord server](https://github.com/JoshuaMeza/HollowBot#add-it-into-your-discord-server)
- [How to create your own?](https://github.com/JoshuaMeza/HollowBot#how-to-create-your-own)
- [Bot files](https://github.com/JoshuaMeza/HollowBot#bot-files)
- [Use cases diagram](https://github.com/JoshuaMeza/HollowBot#use-cases-diagram)
- [Database structure](https://github.com/JoshuaMeza/HollowBot#database-structure)
- [PYDOC Documentation](https://github.com/JoshuaMeza/HollowBot#pydoc-documentation)

## Description

A simple discord bot which plays with you! Feel free of reading the docs or creating your own version.

### Playground

The bot can only execute the command '**--info**' outside of a channel called 'playground'.

### Commands

**--play** <- This command starts a new game.

**--wins** <- This command makes the bot say your global high score.

**--info** <- This command sends a DM to the caster with basic information about the bot.

### Special thanks

The icon is from [yuilero](https://www.instagram.com/yuilero/), you can visit her original post by [clicking here](https://www.instagram.com/p/CHiU20dF16C/?utm_source=ig_web_copy_link).

### Resources

Here are some tutorials and pages that helped me a lot to create this Discord bot:

- [w3schools](https://www.w3schools.com/python/default.asp)
- [Discord Api documentation](https://discordpy.readthedocs.io/en/latest/index.html)
- [freeCodeCamp](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)
- [RealPython](https://realpython.com/how-to-make-a-discord-bot-python/)
- [Lucas Youtube tutorial](https://youtube.com/playlist?list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ)
- [Code With Swastik Youtube tutorial](https://youtube.com/playlist?list=PLoFvxwcEPSPh3pvLwMMq4q_Y-qGpYHGLx)
- [stack overflow](https://stackoverflow.com)
- [MySQL introduction](https://youtu.be/2bW3HuaAUcY)
- [MySQL tutorial](https://youtu.be/7S_tz1z_5bA)
- [Emojipedia](https://emojipedia.org/people/)

## Add it into your Discord server

[Click here to make a new friend!](https://discord.com/api/oauth2/authorize?client_id=794762465883717652&permissions=519232&scope=bot)

## How to create your own?

### Prerequisites

#### Necessary

If you'll work locally, you'll need to prepare this previously, if you are working in a cloud IDE, like [Repl.it](https://repl.it/~), just import the necessary packages into your workspace:

- [x] [Discord account](https://discord.com)
- [x] [Python installed (v3.8.5+)](https://www.python.org/downloads/)
- [x] [Pip installed (v20.0.2+)](https://pypi.org/project/pip/)
- [x] [Discord.py installed (v1.5.1+)](https://pypi.org/project/discord.py/)
- [x] [MySQL Connector installed (v8.0.22+)](https://pypi.org/project/mysql-connector-python/)
- [x] [Dotenv installed (v0.15.0+)](https://pypi.org/project/python-dotenv/)

#### Completely Optional

This is not completely necessary, you may need one or none, depending on what you want to develop and achieve:

- [ ] [Git installed](https://git-scm.com)
- [ ] [Repl.it account](https://repl.it/~)
- [ ] [UptimeRobot account](https://uptimerobot.com)
- [ ] [Visual Studio Code installed](https://code.visualstudio.com)
- [ ] [MySQL Workbench installed](https://www.mysql.com/products/workbench/)

### Steps

1. **Creating a Bot**

First of all, we are going to the [Discord Developer Portal](https://discord.com/developers/applications) to create our discord Bot.

At this moment we have to be in the following page:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_01.png" width="100%">

Now, click the "New Application" button:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_02.png" width="100%">

Put a name and create it, and voalá, you have created your first application:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_03.png" width="100%">

But, it's not a bot yet, go to the section "Bot" of the side bar and transform it:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_04.png" width="100%">

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_05.png" width="100%">

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_06.png" width="100%">

Now, it's time to add it into a Discord server. Go to the section "OAuth2" of the side bar and select the scope 'bot':

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_07.png" width="100%">

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_08.png" width="100%">

Then, give it some basic permissions for now:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_09.png" width="100%">

After that, copy the the link that appeared in the Scopes table and put it in your browser. You'll see a window that asks you if you want to add your recently created bot into a channel, choose one and continue:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_10.png" width="100%">

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_11.png" width="100%">

And you did it! You added your bot into a channel:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_12.png" width="100%">

2. **Bring it to life**

**IMPORTANT!:** To bring it to life, you'll need its token, but be very careful, you cannot put a token anywhere, because if someone gets it they can change the bot's code, and that could be very dangerous!

To get your bot's token, return to the [Discord Developer Portal](https://discord.com/developers/applications), select your bot and copy it:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_13.png" width="100%">

Well, it's time to open your favourite IDE and write some code. At first, open a folder, and create there two files, a `main.py` and a `.env`.

As I said to you, we need to keep secret our token, so, we can use "environment variables" to achieve that (in case you are saving all in a GitHub repository, add a `.gitignore` file and write inside `.env`), because it could be accesed easily in the code and can't be visible in most of the web repositories/IDE's (like [Repl.it](https://repl.it/~)).

Into your `.env` file, write the following:

```
TOKEN=your_token_here
```

And now, open your `main.py` (or the name you liked) to start the creation of your bot. First, we need to import some packages:

```python
import discord                    # Discord api
from discord.ext import commands  # Discord command extension
import os                         # Operative system package, for searching use
from dotenv import load_dotenv    # Package which help us to find the environment variable
```

Rigth now, we still doing nothing with the bot, let's try the following:

```python
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# This creates an object that can manage
# the bot's commands by using a prefix.
prefix = '--'
client = commands.Bot(command_prefix=prefix)

@client.event # Decorator
async def on_ready():
    # This is an coroutine event, and this in special
    # can only be activated when the bot is initialized.
    print('We have logged in as {0.user}'.format(client))

# Load environment variables
load_dotenv()
# client.run('[token]') <- Start the bot which has the
#                          following token
# os.getenv('TOKEN')    <- Operative system, get the
#                          environment variable called TOKEN
client.run(os.getenv('TOKEN'))

# Note: You can freely delete all comments in your deploy.
```

If you run the last code in your computer, you'll be able to read this in your command line, and, see your bot becoming active (you can stop the process by simply killing the terminal):

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_14.png">

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_15.png">

Hey! We are closer to make our bot a little bit more responsive, what if we add it a little command?

```python
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

prefix = '--'
client = commands.Bot(command_prefix=prefix)

# Events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Event activated when a message is sent by anyone
    if message.author == client.user:
        # If the message is from the bot, don't continue
        return

    # Call the activation of commands
    await client.process_commands(message)

# Commands
@client.command()
async def ping(ctx):
    # The function's name is the keyword of your command!
    # It gets activated when the user enters [prefix]say,
    # ie. --ping
    await ctx.send('Pong!')

load_dotenv()
client.run(os.getenv('TOKEN'))
```

Cool, isn't it? if you enter "--ping" the bot will answer you "Pong!":

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_16.png" width="100%">

But, wait, what is ctx? Ctx means context, and **every command** needs to get the context of the call.

And, you may question yourself, what happens if a user sends a command that doesn't exist? In simple words, nothing, you'll see an error message in command line, but (for good practices) we need to manage this kind of errors:

```python
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

prefix = '--'
client = commands.Bot(command_prefix=prefix)

# Events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

@client.event
async def on_command_error(ctx, error):
    # Event which only get activated when getting an error
    if isinstance(error, commands.CommandNotFound):
        # Here we are creating an embed message to notify the error
        embed = discord.Embed(
            title='Oops!',
            description='Error: {}'.format(error),
            colour=discord.Colour.from_rgb(61, 64, 91)
        )
        await ctx.send(embed=embed, delete_after=10.0)

# Commands
@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

load_dotenv()
client.run(os.getenv('TOKEN'))
```

Try out a non existing command, like '--test':

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_17.png" width="100%">

2. **Modularity**

To divide the program into multiple small parts, which increase readability and maintainability, that do specific tasks we can use Cogs extension.

But, what we could divide and how? My friend, we can make the commands a different part of the main code, making a cleaner work and making easier to include more commands! Follow me and see how:

First, create a subdirectory and add two new python files there, you will have something like this:

```
- src
  + main.py
  + .env
  - modules
    + ping.py
    + say.py
```

And, in the `main.py` file we are going to add a "reading" process and delete the command '--ping' (save it for `ping.py`):

```python
import discord
from discord.ext import commands
import os
import sys #new
from dotenv import load_dotenv

# Initialization
prefix = '--'
client = commands.Bot(command_prefix=prefix)

# Reading process
# NOTE: If you are running this from vs code directly, it may fail, do
# the execution manually from the terminal!
# Why it may fail? Since VS Code will try to execute the program from a
# directory that is 'inside' the file, this process will never find the
# subdirectory.
# If you have this problem, set your terminal (by cd command)
# in the source ('src') directory.
for filename in os.listdir('modules/'):
    # os.listdir('PATH') returns a list with all items inside the path
    if (filename.endswith('.py')):
        # ^ If it is a python file, continue the process...
        # load_extension adds the code from the file to the main program
        # during the execution, it's similar to importing, but you don't
        # have to cast the object to check if the command inside of it
        # was called.
        client.load_extension('modules.{}'.format(filename[:-3]))

# Events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title='Oops!',
            description='Error: {}'.format(error),
            colour=discord.Colour.from_rgb(61, 64, 91)
        )
        await ctx.send(embed=embed, delete_after=10.0)

load_dotenv()
client.run(os.getenv('TOKEN'))
```

Then, go to `ping.py` file and write the following code:

```python
import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        # If this module is charged, will print it
        print('Ping module loaded!')

    # Command
    # aliases adds new kewwords to your command
    @commands.command(aliases=['PING'])
    async def ping(self, ctx):
        # Add a reaction to the command ¬
        await ctx.message.add_reaction('🏓')
        await ctx.send('Pong!')

# Needed to initialize
def setup(client):
    client.add_cog(Ping(client))
```

And finally, go to `say.py`:

```python
import discord
from discord.ext import commands


class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        # If this module is charged, will print it
        print('Say module loaded!')

    # Command
    @commands.command(aliases=['SAY'])
    async def say(self, ctx, *, message=""):
        # Say the words that follow the command
        await ctx.send(message)

# Needed to initialize
def setup(client):
    client.add_cog(Say(client))
```

And now, it's time to try our new bot:

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/scrn_18.png" width="100%">

3. **Saving score**

At this moment you know the basics of creating Discord bots, by now you can try using the code that I made for HollowBot and adding them your own commands into the modules.

Note that HollowBot saves and retrieves the score by using the class Connector, that also needs some environment variables, you have to update them:

```
TOKEN=your_token_here
HOST=your_host_here
MYSQLUS=your_user_name_here
PASSWD=your_password_here
DB=your_database_name_here
```

In case you can't or don't want to use a database, replace the following code from `Play.py`:

```python
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
```

To this:

```python
if (flagDoSave):
    try:
        # 'a' means append into the file
        with open('wins.txt', 'a') as wins:
            wins.write(str(ctx.author.id) + '\n')
    except Exception as e:
        embed = discord.Embed(
            title='Oops!',
            description='Sorry, but I can\'t save your victory in my Legends Journal, I think I lost my pen...',
            colour=discord.Colour.red()
        )
        await ctx.send(embed=embed, delete_after=10.0)
```

And the following code from `Wins.py`:

```python
score = -1

try:
    c = Connector()
    score = c.getWins(str(ctx.author.id))
except Exception as e:
    score = -1
```

To this:

```python
score = 0

try:
    # 'r' means read the file
    with open('wins.txt', 'r') as wins:
        for line in wins:
            temp = line.split('\n')

            if (temp[0] == str(ctx.author.id)):
                score += 1
except Exception as e:
    score = 0
```

Then you can leave your environment variables file the same as it was at the beginning:

```
TOKEN=your_token_here
```

And finally, do not forget to delete the imports to `Connector.py`, and do not include that file in the modules directory.

All of this will change the way of storing your data, at this moment and forward the bot will create a `wins.txt` file in which, everytime a user wins the game, will append their user id instead of saving the victories amount in a database.

4. **Hosting your bot**

And last but not least, hosting. I feel like the method that used [freeCodeCamp](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) in their tutorial is the easiest and free way to host our little creation, you can find all the instructions there:

- [freeCodeCamp Tutorial](https://youtu.be/SPTfmiYiuok?t=3522)

## Bot files

- [Main](https://github.com/JoshuaMeza/HollowBot/blob/master/code/main.py)
- [Connector](https://github.com/JoshuaMeza/HollowBot/blob/master/code/modules/Connector.py)
- [Info](https://github.com/JoshuaMeza/HollowBot/blob/master/code/modules/Info.py)
- [Play](https://github.com/JoshuaMeza/HollowBot/blob/master/code/modules/Play.py)
- [Wins](https://github.com/JoshuaMeza/HollowBot/blob/master/code/modules/Wins.py)

## Use cases diagram

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/UseCases.png" width="100%">

> Icons designed by [Flat Icons](https://www.flaticon.es/autores/flat-icons) from [Flaticon](https://www.flaticon.es/), and background picture by [Roberto Nickson](https://www.pexels.com/es-es/foto/mar-amanecer-paisaje-cielo-2775196/) from [Pexels](https://www.pexels.com/es-es/).

## Database structure

The database only has one table which stores the user id of a player and their global score.

<img src="https://github.com/JoshuaMeza/HollowBot/blob/master/Resources/DataBase.png">

## PYDOC Documentation

[Click here to download it.](https://github.com/JoshuaMeza/HollowBot/blob/master/DocumentationPYDOC.zip?raw=true)
