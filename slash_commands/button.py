import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui.item import Item

class Button(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView())

    @slash_command()
    async def button1(self,ctx:commands.Context):
        await ctx.respond('Klick mich', view=TutorialView())

    @slash_command()
    async def url_button(self,ctx:commands.Context):
        button = discord.ui.Button(label='Ich bin ein Url Button',url='https://sssssssss.de')
        view = discord.ui.View()
        view.add_item(button)
        await ctx.respond('Klick mich', view=view)

    @slash_command()
    async def button2(self,ctx:commands.Context, label:discord.Option(str, 'name of the button')):
        button = TutorialButton(label)
        view = discord.ui.View()
        view.add_item(button)
        await ctx.respond('Klick mich', view=view)

def setup(bot:discord.Bot):
    bot.add_cog(Button(bot))

class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Klick mich 1', style=discord.ButtonStyle.primary, custom_id='button1', row=1)
    async def button_callback1(self,button,interaction):
        await interaction.response.send_message('Ja du hast mich geklickt.')

    @discord.ui.button(label='Klick mich yo', style=discord.ButtonStyle.primary, custom_id='button2', row=2)
    async def button_callback2(self,button,interaction):
        button.disabled = True
        button.label = 'Tja'
        await interaction.response.edit_message(view=self)

class TutorialButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hey', ephemeral=True)
