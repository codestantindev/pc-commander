from settings import *

class Screenshot(ezcord.Cog):

    @slash_command(description="➛│Macht einen Screenshot!")
    @commands.cooldown(1, 5)
    async def screenshot(self, ctx: discord.ApplicationContext):
        pyautogui.screenshot("img/screenshot.png")
        embed = discord.Embed(
            title="Screenshot",
            description="Du hast einen Screenshot erstellt!",
            color=discord.Color.blurple()
        )
        try:
            embed.set_thumbnail(url=ctx.user.display_avatar)
        except:
            pass
        file = discord.File(f"img/screenshot.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        
        await ctx.respond(embed=embed, file=file)

def setup(bot):
    bot.add_cog(Screenshot(bot))