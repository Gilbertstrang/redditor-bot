import random
from discord.ext import commands

with open("./data/wordbank.txt", encoding="utf8") as f:
        words = f.read().split(', ')



HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word = words[random.randint(0, len(words) - 1)]
user_guesses = list()


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="Hangman game. !hg [letter]")
    async def hg(self, ctx, guess: str):
        global word
        progress_word = ""
        guess = guess.lower()
        mistakes = 0
        if len(user_guesses) >= 6:
            await ctx.send(HANGMANPICS[6])
            await ctx.send("Game over. My Crystal Braves....")
            return

        for c in word.lower():
            if guess == c or c in user_guesses:
                progress_word += c
            else:
                await ctx.send(HANGMANPICS[mistakes])
                progress_word += "\_."
                mistakes += 1

                
        user_guesses.append(guess)

        if guess == word:
            await ctx.send("By the Twelve, you won!")
            word = words[random.randint(0, len(words) - 1)]
        else:
            await ctx.send("Progress: %s" % progress_word)



def setup(bot):
    bot.add_cog(Games(bot))