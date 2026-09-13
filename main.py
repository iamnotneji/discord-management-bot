import discord
from discord.ext import commands
import os
from config import DISCORD_TOKEN, PREFIX

# Set up bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Load cogs (command modules)
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename}')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('------')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(DISCORD_TOKEN)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
