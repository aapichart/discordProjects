from os import wait
import nextcord
from nextcord import interactions
from nextcord import embeds
from nextcord.enums import ButtonStyle
from nextcord.ext import commands

class nameUI(nextcord.ui.TextInput):
    def __init__(self): 
        super().__init__(
            label="Name",
            min_length=2,
            max_length=8,
            placeholder=""
        )
    async def callback(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("This is a test") 

class loginform(nextcord.ui.Modal):
    def __init__(self, display_name, user_icon_url, guild_icon_url):
        super().__init__(
            "LoginForm"
        )
        self.display_name=display_name
        self.user_icon_url=user_icon_url
        self.guild_icon_url=guild_icon_url
        self.name_ui=nameUI()
        self.answer_ui = nextcord.ui.TextInput(
            label="Reason",
            style=nextcord.TextInputStyle.short
        )
        self.answer1_ui = nextcord.ui.TextInput(
            label="Reason1",
            style=nextcord.TextInputStyle.short
        )
        self.answer2_ui = nextcord.ui.TextInput(
            label="Reason2",
            style=nextcord.TextInputStyle.short
        )
        self.answer3_ui = nextcord.ui.TextInput(
            label="Reason3",
            style=nextcord.TextInputStyle.short
        )
        self.add_item(self.name_ui)
        self.add_item(self.answer_ui)
        self.add_item(self.answer1_ui)
        self.add_item(self.answer2_ui)
        self.add_item(self.answer3_ui)
    
    answer1={"name":"", "reason":""}
    async def callback(self, interaction: nextcord.Interaction):
        self.answer1["name"]=self.name_ui.value
        self.answer1["reason"]=self.answer_ui.value
        
        #  send information from modal to check-in channel
        emb2=nextcord.Embed(title="Information", colour=0xe74c3c)
        emb2.add_field(name="Information", value=self.answer1)
        emb2.set_footer(text=f"Requested by {self.display_name}", icon_url=self.user_icon_url)
        emb2.set_thumbnail(url=self.guild_icon_url)
        channel = nextcord.utils.get(interaction.guild.channels, name="check-in")
        await channel.send(f" {self.answer1}", embed=emb2)

        await interaction.response.send_message(f" From modal answer={self.answer1}", ephemeral=True)


class checkOutButton(nextcord.ui.Button):
    def __init__(self, display_name, user_icon_url, guild_icon_url):
        self.display_name=display_name
        self.user_icon_url=user_icon_url
        self.guild_icon_url=guild_icon_url
        super().__init__(label="Check-out Req", style=nextcord.ButtonStyle.blurple)

    async def callback(self, interaction: nextcord.Interaction):
        loginfrm=loginform(self.display_name, self.user_icon_url, self.guild_icon_url)
        await interaction.response.send_modal(loginfrm)


class checkInButton(nextcord.ui.Button):
    def __init__(self, display_name, user_icon_url, guild_icon_url):
        self.display_name=display_name
        self.user_icon_url=user_icon_url
        self.guild_icon_url=guild_icon_url
        super().__init__(label="Check-in Req", style=nextcord.ButtonStyle.green)

    async def callback(self, interaction: nextcord.Interaction):
        loginfrm=loginform(self.display_name, self.user_icon_url, self.guild_icon_url)
        await interaction.response.send_modal(loginfrm)

class mainView(nextcord.ui.View):
    def __init__(self, display_name, user_icon_url, guild_icon_url):
        self.display_name=display_name
        self.user_icon_url=user_icon_url
        self.guild_icon_url=guild_icon_url
        super().__init__()
        #  self.add_item(surveySelect())
        self.add_item(checkOutButton( self.display_name, self.user_icon_url, self.guild_icon_url))
        self.add_item(checkInButton( self.display_name, self.user_icon_url, self.guild_icon_url))

    answer1={}
    async def callback(self, interaction:nextcord.Interaction):
        print(f" view callback information {self.answer1}")
        await interaction.response.send_message(f"answer={self.answer1}")
    
class permissionReqView(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       print("permissionReqView is loaded .....! ") 
    
    @commands.command(name='permreq')
    async def permreq(self, ctx):
        emb=nextcord.Embed(title="Vehicle Control Action: \n ขออนุญาตินำรถยนต์ เข้า - ออก:  ", colour=0xe74c3c)
        emb.set_footer(text=f"Requested by {ctx.message.author.display_name}", icon_url=ctx.author.avatar)
        emb.set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed=emb)

        display_name=ctx.author.display_name
        user_icon_url=ctx.message.author.avatar
        guild_icon_url=ctx.guild.icon
        view=mainView(display_name, user_icon_url, guild_icon_url)
        await ctx.send(f'โปรดเลือก: ', view=view) 
        #  send information from modal to channel
        #  emb2=nextcord.Embed(title="Information", colour=0xe74c3c)
        #  emb2.add_field(name="Information", value=view.answer1)
        #  emb2.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.message.author.avatar)
        #  emb2.set_thumbnail(url=ctx.guild.icon)
        #  #  channel=nextcord.utils.get(ctx.guild.channels, name="Check-in")
        #  await ctx.send(embed=emb2)


def setup(bot):
    bot.add_cog(permissionReqView(bot))
    

############ unused code but keep for reference ##################


    #  async def response_toAnswer(self, interaction:nextcord.Interaction, choice):
        #  size = len(self.children)
        #  print(f"the number of children : {size}")
        #  for x in range(self.size_survey): 
            #  self.children[x].disabled=True
            #  surveyItem1=surveySelect() 
            #  self.add_item(surveyItem1)
            #  await interaction.message.edit(view=self)
            #  await interaction.response.defer() 
            #  if x == self.size_survey-1:
                #  print("This is the last component in survey ......")
                #  await interaction.response.send_message(self.answer1) 
        #  self.stop()

#  class surveySelect(nextcord.ui.Select):
    #  def __init__(self):
        #  options=[
            #  nextcord.SelectOption(label="1", value="1"),
            #  nextcord.SelectOption(label="2", value="2"),
            #  nextcord.SelectOption(label="3", value="3"),
        #  ]
        #  super().__init__(options=options, min_values=1, max_values=1, placeholder="What is your choices?")
    #  async def callback(self, interaction:nextcord.Interaction):
        #  loginfrm=loginform()
        #  await interaction.response.send_modal(loginfrm)
        
