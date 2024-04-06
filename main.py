from settings import *

bot = ezcord.Bot(intents=discord.Intents.all())

if __name__ == "__main__":
    bot.load_cogs("cogs")
    ld()
    bot.run(os.getenv("TOKEN"))