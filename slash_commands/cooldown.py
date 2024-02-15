import discord
from discord.ext import commands
from discord.commands import slash_command

class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hey(self,ctx):
        await ctx.respond('HEY')
        
def setup(bot):
    bot.add_cog(Cooldown(bot))