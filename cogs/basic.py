import discord
from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "Repeats.")
    async def say(self, ctx, *, message):
        await ctx.send(message)

    @commands.command(brief = "Pray.")
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            channel = member.dm_channel
            if channel is None:
                channel = await member.create_dm()
            await channel.send("%s wants you to pray return to the Waking Sands." % ctx.author.name)
        else:
            await ctx.send("You must needs use @mention.")

def setup(bot):
    bot.add_cog(Basic(bot))