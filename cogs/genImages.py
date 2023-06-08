from PIL.ImageFont import ImageFont
import qrcode
from PIL import Image, ImageDraw, ImageFont
from nextcord import File
from nextcord.ext import commands

class genImages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_ready(self):
       print("genImages is loaded .....! ") 
    
    @commands.command()
    async def getqr(self, ctx, *args):
        message = " ".join(args) 
        img = qrcode.make(message)
        img.save('./images/replyImage.jpg')

        with open("./images/replyImage.jpg", "rb") as f:
            img = File(f)
            await ctx.send(file=img)

    @commands.command()
    async def getpass(self, ctx, *args):
        message = " ".join(args)
        #Read waiting.jpg as a background images
        imgBackGround=Image.open('./images/waiting.jpg')
        imgFinal=imgBackGround.copy()

        #Draw text on image
        draw=ImageDraw.Draw(imgFinal)

        ThaiFontPath='/usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf'
        EngFontPath='/home/apichart/.local/share/fonts/DejaVuSans.ttf'

        fontThai=ImageFont.truetype(ThaiFontPath, 25)
        font=ImageFont.truetype(EngFontPath, 25)
        draw.text((40,30), " รออนุมัติ ", font=fontThai, fill="white")
        draw.text((40,70), " SanguanTAS co.,ltd.", font=font, fill="white")
        draw.text((350,70)," วันที่ ", font=fontThai, fill="white")
        draw.text((425,70)," 01/05/66 ", font=font, fill="white")
        #Gen qr code image to merge with background image
        qr = qrcode.QRCode(box_size=4)
        qr.add_data(message)
        qr.make()
        img = qr.make_image()
        imgFinal.paste(img, (500,250))
        imgFinal.save('./images/replyImage.jpg')

        with open("./images/replyImage.jpg", "rb") as f:
            img1 = File(f)
        await ctx.send(file=img1)

def setup(bot):
    bot.add_cog(genImages(bot))
