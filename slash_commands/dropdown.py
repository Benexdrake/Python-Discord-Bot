import discord
from discord.ext import commands
from discord.commands import slash_command


options= [
    discord.SelectOption(label='Python', description='Python Beschreibung', emoji='😂'),
    discord.SelectOption(label='C#', description='C# Beschreibung', emoji='😍'),
    discord.SelectOption(label='Typescript', description='Typescript Beschreibung', emoji='🥰')
]

class Dropdown(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command()
    async def create_dropdown1(self,ctx):
        await ctx.respond("Wähle Programmiersprachen aus", view=TutorialView())

    @slash_command()
    async def create_dropdown2(self,ctx):
        select = TutorialSelect()
        view = discord.ui.View(timeout=None)
        view.add_item(select)

        await ctx.respond(view=view)
        
def setup(bot):
    bot.add_cog(Dropdown(bot))




class TutorialSelect(discord.ui.Select):
    def __init__(self):
        super().__init__(min_values=1,
        max_values=1,
        placeholder='Triff eine Auswahl',
        options=options,
        custom_id='dropdowntest123')

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Du hast {self.values[0]} gewählt', ephemeral=True)

class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout==None)

    @discord.ui.select(
        min_values=1,
        max_values=2,
        placeholder='Triff eine Auswahl',
        options=options,
        custom_id='dropdowntest123'
    )

    async def select_callback(self,select,interaction):
        s=''
        for auswahl in select.values:
            s += f'- {auswahl}\n'

        await interaction.response.send_message(f'Du hast folgendes ausgewählt:\n{s}', ephemeral=True)