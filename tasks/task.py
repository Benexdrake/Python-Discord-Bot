import discord
from discord.ext import commands, tasks

from datetime import time,timezone

class Task(commands.Cog):
    def __init__(self, bot:discord.bot):
        self.bot = bot

    #@commands.Cog.listener()
    #async def on_ready(self):
        #self.tasktimer.start()

    @tasks.loop(seconds=2)
    async def task(self):
        if self.task.current_loop == 0:
            return
        print('test')

    @tasks.loop(time=time(19,48, tzinfo=timezone.utc))
    async def tasktimer(self):
        print('Hello World')

def setup(bot:discord.bot):
    bot.add_cog(Task(bot))