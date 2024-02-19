import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ext.pages import Paginator, Page

class PageTest(commands.Cog):
    def __init__(self,bot:discord.Bot):
        self.bot = bot

    @slash_command()
    async def page(self,ctx:commands.Context):

        pages = [
            Page(content='HALLO'),
            Page(content='Welt')
        ]

        paginator = Paginator(pages=pages)
        paginator.remove_button('first')
        paginator.remove_button('last')

        await paginator.respond(ctx.interaction, ephemeral=True)

    @slash_command()
    async def memberlist(self,ctx:commands.Context):
        members = ctx.guild.members
        pages = []
        description = ''

        for i,member in enumerate(members):
            description += f'{i+1}. {member}\n'
            if (i+1) % 10 == 0 or i == len(members) -1:
                embed = discord.Embed(title= 'Member List', color=discord.Color.green(), description=description)
                embed.set_thumbnail(url=ctx.guild.icon.url)
                #pages.append(Page(embeds=[embed]))
                pages.append(embed)
                description = ''
        paginator = Paginator(pages=pages)
        await paginator.respond(ctx.interaction, ephemeral=True)


def setup(bot:discord.Bot):
    bot.add_cog(PageTest(bot))