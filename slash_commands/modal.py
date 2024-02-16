import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui.input_text import InputText

class ModalTest(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command()
    async def modal(self,ctx):
        modal = TutorialModal(title='Erzeuge ein Embed')
        await ctx.send_modal(modal)

    @slash_command()
    async def button_modal(self,ctx):
        await ctx.respond('Hey', view=TutorialView())
        
def setup(bot):
    bot.add_cog(ModalTest(bot))

class TutorialModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Embed Titel",
                placeholder='Placeholder'
            ),
            discord.ui.InputText(
                label='Embed Beschreibung',
                placeholder='Placeholder',
                style=discord.InputTextStyle.long
            ),
            *args,
            **kwargs)
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{self.children[0].value} - {self.children[1].value}')
    

class TutorialView(discord.ui.View):
    @discord.ui.button(label='Open Modal')
    async def button_callback(self,button, interaction):
        await interaction.response.send_modal(TutorialModal(title='Test Modal'))