import discord
from discord.commands import Option

def SlashHandler(bot):
    @bot.slash_command(description='Grüße einen User')
    async def greet(ctx, user: Option(discord.Member, "Der User, den du grüßen möchtest")):
        await ctx.respond(f'Hallo {user.mention}')

    @bot.slash_command(description='Lass den Bot eine Nachricht senden')
    async def say(ctx, text: Option(str, 'Der Text, den du senden möchtest'), channel: Option(discord.TextChannel)):
        await channel.send(text)
        await ctx.respond('Die Nachricht wurde gesendet', ephemeral=True)

    @bot.slash_command(descriptions='Zeige Infos über einen User', name='userinfo')
    async def info(ctx,alter:Option(int, 'Das Alter', min_value=1, max_value=99),user: Option(discord.Member, 'Gib einen User ein', default=None)):
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
        embed.add_field(name='Alter', value=alter)

        embed.set_thumbnail(url=user.display_avatar.url)

        embed.set_footer(text='Footer Beispiel')

        await ctx.respond(embed=embed)