import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option

class Kick(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot
    @slash_command(description= 'Kicke Member')
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def kick(self,ctx:commands.Context,member: Option(discord.Member, 'Gib einen User ein')):
        try:
            await member.kick()
            await ctx.respond(f'{member.mention} wurde gekickt')
        except discord.Forbidden as e:
            await ctx.respond(e, ephemeral=True)


def setup(bot:discord.Bot):
    bot.add_cog(Kick(bot))