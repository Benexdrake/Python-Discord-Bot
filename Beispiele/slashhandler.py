import discord
from discord.commands import Option

def SlashHandler(bot):
    @bot.slash_command(description='Grüße einen User')
    @discord.option('user', description='wähle einen user', choices=['ja','nein'])
    async def greet(ctx, user: discord.User, auswahl:str='ja'):
        await ctx.respond(f'Hallo {user.mention}')