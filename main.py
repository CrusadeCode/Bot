import discord, os, audioop, logic as l
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv ()
token = os.getenv ("dt")

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command(name = "coin")
async def luck(ctx):
    await ctx.send(l.coin())
bot.run(token)