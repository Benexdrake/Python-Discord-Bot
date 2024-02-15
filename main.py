import discord
import os
from dotenv import load_dotenv

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    status = discord.Status.dnd
    activity = discord.Activity(type=discord.ActivityType.playing, name='sich am Sack')

    bot = discord.Bot(intents=intents, debug_guilds=[998136328032112671], status=status, activity=activity)

    loading(bot, 'tasks')
    loading(bot, 'events')
    loading(bot, 'slash_commands')

    load_dotenv()
    bot.run(os.getenv('TOKEN'))
    

def loading(bot, folder):
    for filename in os.listdir(f"{folder}"):
        if filename.endswith('.py'):
            print(f'Loading {folder}: {filename[:-3]}')
            bot.load_extension(f'{folder}.{filename[:-3]}')

main()

  
  