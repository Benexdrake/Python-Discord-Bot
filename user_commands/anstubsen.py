import discord
from discord.ext import commands
from discord.commands import user_command
from discord.commands import Option

class Anstubsen(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @user_command()
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def anstubsen(self,ctx:commands.Context,member:discord.member):
        await ctx.respond(f'{ctx.author.mention} hat {member.mention} angestubst')


def setup(bot):
    bot.add_cog(Anstubsen(bot))