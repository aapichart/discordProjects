import discord
from discord.ext import commands
from apikey import BOTTOKEN


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("---------------------------")
    print("The Bot is ready for use!! ")
    print("---------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, My name is AlphaBot. I'm here to help you. ")

client.run(BOTTOKEN)


    
