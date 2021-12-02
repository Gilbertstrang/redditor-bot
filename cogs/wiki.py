import discord
import sys
import requests
import markovify

from discord.ext import commands


class Markov(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "Wikipedia.")
    async def wiki(self, ctx):
            r = requests.get("https://en.wikipedia.org/wiki/special:random")
            await ctx.send(r.url)


def setup(bot):
    bot.add_cog(Markov(bot))