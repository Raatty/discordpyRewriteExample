import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="t&", description="a very simple bot")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(os.getenv('TOKEN'))