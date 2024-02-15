import discord
from discord.ext import commands
from discord.commands import user_command
from discord.commands import Option

class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @user_command()
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def delete(self,ctx,member):
        ctx.message.delete()


def setup(bot):
    bot.add_cog(Delete(bot))