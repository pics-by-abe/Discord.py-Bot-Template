import discord
from discord.ext import commands
from pathlib import Path

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    for file in Path("cogs").glob("*.py"):

        name = file.stem

        if name.startswith('__'):
            continue

        bot.load_extension(f"cogs.{name}")

    print("Ready to rumble")




bot.run("NDk3NDI3NTE0ODg5ODYzMTY5.W7YveQ.k0BfQguXW4i9-nHYUju1ATRVXkk")
#bot.run("Your Token from: https://discord.com/developers/applications")