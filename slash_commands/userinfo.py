import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.commands import Option

class UserInfo(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot
    @slash_command()
    async def userinfo(self,ctx:commands.Context,user: Option(discord.Member, 'Gib einen User ein', default=None)):
        if user is None:
            user = ctx.author

        embed = discord.Embed(
            title=f'Infos über {user.name}',
            description=f'Hier siehst du alle Details über {user.mention}',
            color=discord.Color.red()
        )

        time = discord.utils.format_dt(user.created_at, 'R')

        embed.add_field(name='Account erstellt', value=time, inline=False)
        embed.add_field(name='ID', value=user.id)

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.set_footer(text='Footer Beispiel')

        await ctx.respond(embed=embed)


def setup(bot:discord.Bot):
    bot.add_cog(UserInfo(bot))