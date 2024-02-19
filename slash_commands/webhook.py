import discord
from discord.ext import commands
from discord.commands import slash_command

import aiohttp

import os
from dotenv import load_dotenv

class WebHook(commands.Cog):
    def __init__(self,bot:discord.Bot):
        self.bot = bot

    load_dotenv()

    @slash_command()
    async def webhook_old(self,ctx:discord.ApplicationContext):
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(os.getenv('WEBHOOK'), session=session, bot_token=self.bot.http.token)
            await webhook.send('Ich bin ein Webhook Test', username=ctx.author.name, avatar_url=ctx.author.avatar.url)
        await ctx.respond('Webhook gesendet')
        
    @slash_command()
    async def webhook_create(self,ctx:discord.ApplicationContext):
        webhook = await ctx.channel.create_webhook(name='Pupskopf')

        await webhook.send(
            'Ich bin ein Webhook',
            username=ctx.author.name, 
            avatar_url=ctx.author.avatar.url,
            wait=True,
            view=TutorialView()
        )
        await ctx.respond('Webhook Created', ephemeral=True)

def setup(bot):
    bot.add_cog(WebHook(bot))

class TutorialView(discord.ui.View):
    @discord.ui.button(label='Krass')
    async def callback(self,button,interaction:discord.Interaction):
        await interaction.response.send_message('Fortnite ist Dreck', ephemeral=True)