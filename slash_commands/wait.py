import discord
from discord.ext import commands
from discord.commands import slash_command

import asyncio

class Wait(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command()
    async def wait(self,ctx):
        await ctx.respond('Gib eine Zahl ein')

        def check(message):
            return message.author == ctx.author and message.content.isdigit()

        try:
            answer = await self.bot.wait_for('message', timeout=5.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You are to slow')
            return
        await answer.reply(f'Du hast die Zahl {answer.content} eingegeben')
        
def setup(bot):
    bot.add_cog(Wait(bot))