from settings import *

class Wallpaper(ezcord.Cog):

    @slash_command(description="➛│Ändert den Hintergrund!")
    async def set_wallpaper(self, ctx: discord.ApplicationContext, img: discord.Attachment):
        await ctx.defer()
        allowed_img_endings = ["png", "jpg", "jpeg"]

        file_extension = img.filename.split(".")[-1].lower()

        if file_extension not in allowed_img_endings:
            await ctx.respond(
                f"Du kannst nur Bilder mit der Endung `.png` `.jpg` und `.jpeg` hochladen!", ephemeral=True
            )
            return
        try:
            img_dir = "img"
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)

            file_path = os.path.join(img_dir, img.filename)
            await img.save(file_path)

            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, os.path.abspath(file_path), 3
            )
            await asyncio.sleep(1)
            pyautogui.hotkey('win', 'd')
            await asyncio.sleep(1)
            pyautogui.screenshot("img/screenshot.png")
            embed = discord.Embed(
                title="Wallpaper",
                description="Du hast den Hintergrund geändert!",
                color=discord.Color.blurple()
            )
            try:
                embed.set_thumbnail(url=ctx.user.display_avatar)
            except:
                pass

            file = discord.File(f"img/screenshot.png", filename="image.png")
            embed.set_image(url="attachment://image.png")
            await ctx.respond(embed=embed, file=file)
            os.remove(f"img/{img.filename}")

        except Exception as e:
            print(e)
            await ctx.respond(
                "Irgendwas ist schiefgelaufen... Kontaktiere den Bot Owner!", ephemeral=True
            )

def setup(bot):
    bot.add_cog(Wallpaper(bot))