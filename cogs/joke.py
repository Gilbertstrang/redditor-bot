
from discord.ext import commands
from utils import markov, jokes

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Alphinaud gives his wisdom.")
    async def quote(self, ctx):
        async with ctx.channel.typing():    
            first = markov()
            await ctx.send(first)
    
    @commands.command(brief="Tells a joke")
    async def joke(self, ctx):
        async with ctx.channel.typing():    
            first = jokes()
            await ctx.send(first)

def setup(bot):
    bot.add_cog(Joke(bot))