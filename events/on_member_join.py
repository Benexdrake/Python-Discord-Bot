import discord
from discord.ext import commands

class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        embed = discord.embed(
            title='Willkommen',
            description=f'Hey {member.mention}',
            color=discord.Color.orange()
        )

        channel = await self.bot.fetch_channel(1044857228697554975)

        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(OnMemberJoin(bot))