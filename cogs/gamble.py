from logging import NullHandler
import random
import re
import emoji

from discord.ext import commands
from utils import dice_roll, adv_roll, dadv_roll

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    global emo
    emo = emoji.emojize(":game_die:")

    @commands.command(brief="Gives a random number between 1 and input(otherwise 1000)")
    async def rand(self, ctx, *, num):
        if num.isnumeric():
            num = int(num)
            x = random.randrange(1, num+1)
            dice = emoji.emojize(":game_die:")
            y = f"{dice} I have rolled {x}, Warrior of Light."
            await ctx.send(emoji.emojize(y))
        elif num == "" or num == None or num == " ":
            x = random.randrange(1, 1000)
            dice = emoji.emojize(":game_die:")
            y = f"{dice} I have rolled {x}, Warrior of Light."
            await ctx.send(emoji.emojize(y))
        else:
            await ctx.send("Pray give me a number.")
    
    @commands.command(brief="!r [dice] i.e. 2d20+3")
    async def r(self,ctx, *, numb):
        
        faces, mod, crit, reroll = dice_roll(numb)
        result = sum(faces) + mod
        a = ""
        b = ""
        if crit > 0:
            a = " **CRITICAL HIT!**" 
        if reroll > 0:
            b = f" *You rerolled* **{reroll}** *1s.*"
        rolls = f"{emo}You roll {faces}.{a}{b} Total of **{result}**!!"
        await ctx.send(rolls)
        if numb == False:
            await ctx.send("No die to roll.")
    
    @commands.command(brief="Roll with advantage. i.e !ar 1d20")
    async def ar(self, ctx, *, numb):
        roll, mod, faces = adv_roll(numb)
        result = int(roll) + int(mod)
        
        rolls = f"{emo}You roll {faces} with advantage. Total of **{result}**!!"
        await ctx.send(rolls)
        if numb == False:
            await ctx.send("No die to roll.")
    
    @commands.command(brief="Roll with disadvantage. i.e. !dr 1d20")
    async def dr(self, ctx, *, numb):
        roll, mod, faces = dadv_roll(numb)
        result = int(roll) + int(mod)
        
        
        rolls = f"{emo}You roll {faces} with disadvantage. Total of **{result}**!!"
        await ctx.send(rolls)
        if numb == False:
            await ctx.send("No die to roll.")


def setup(bot):
    bot.add_cog(Gamble(bot))