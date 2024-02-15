import discord
from discord.commands import Option

def EventHandler(bot):

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} ist Online')


    @bot.event
    async def on_message(msg):
        if msg.author.bot:
            return
        await msg.channel.send('Python yay')

    @bot.event
    async def on_message_delete(msg):
        await msg.channel.send(f'Eine Nachricht von {msg.author} wurde gelöscht: {msg.content}')