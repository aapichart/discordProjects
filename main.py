import asyncio
import textwrap
import os

import nextcord 
from nextcord.ext import commands
from apikey import BOTTOKEN

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print("---------------------------")
    print("The Bot is ready for use!! ")
    print("---------------------------")

@bot.event
async def on_message(message):
    commandStr = ("!hello", "!showcmd", "!getqr", "!getpass", "!permreq")
    if message.author == bot.user:
        return
    if message.content.startswith(commandStr):
        await message.channel.send("Processing ....", delete_after=1)
        await bot.process_commands(message)
    else:
        await message.channel.send("I'm sorry.  I don't understand your order!! Please re-enter your command in all lowercase letters!! ")

def load():
    print("Setting up ...... ") 
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print(f'filename: {filename}')
            print(f'cogs.{filename[:-3]}')
            bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command(name='hello')
async def hello(ctx):
    message = f"Hello!! I'm AlphoBot. I'm here to help you. type '!showcmd' for show commands." 
    await ctx.send(message)

def showcmdMsg(): 
    command_message = command_message = f"""
    * All commands should be written in all low letters *
    use "!" + [command] : These are the commands
    1. hello
    2. showcmd
    3. getqr + [message]
    4. getpass + [message]
    5. permreq + [message]
    """
    return textwrap.dedent(command_message)

@bot.command(name='showcmd')
async def showcmd(ctx):
    message = showcmdMsg() 
    await ctx.send(message)

async def main():
    load() 
    await bot.start(BOTTOKEN)

if __name__ == "__main__":
    asyncio.run(main()) 



    
