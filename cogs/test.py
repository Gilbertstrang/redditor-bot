from discord.ext import commands
from utils import text_to_owo

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="OwO whats this?")
    async def owo(self, ctx, *, message):
        await ctx.send(text_to_owo(message))

def setup(bot):
    bot.add_cog(Test(bot))