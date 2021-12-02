import random
import aiohttp
from discord.ext import commands
import discord
import praw

from settings import REDDIT_APP_ID, REDDITAPP_SECRET, REDDIT_SUBREDDITS, REDDIT_NSFW_SUBREDDITS

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDITAPP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDITAPP_SECRET, user_agent="Alphinaud:%s:0.5" % REDDIT_APP_ID)

    @commands.command(brief="Random meme from Reddit. !red [sub]")
    async def red(self, ctx, subreddit: str = ""):
        async with ctx.channel.typing():
            if self.reddit:
                nsfw_flag = False
                chosen_subreddit = REDDIT_SUBREDDITS[random.randint(0, len(REDDIT_SUBREDDITS) -1)]
                if subreddit:
                    if subreddit not in REDDIT_SUBREDDITS:
                        chosen_subreddit = subreddit
                    elif subreddit in REDDIT_NSFW_SUBREDDITS:
                        chosen_subreddit = subreddit
                        nsfw_flag = True
                    elif subreddit in REDDIT_SUBREDDITS:
                        chosen_subreddit = subreddit
                    else:
                        await ctx.send("Pray choose a subreddit from this list: %s" % ", ".join(REDDIT_SUBREDDITS))
                        return
                
                if nsfw_flag:
                    if not ctx.channel.is_nsfw():
                        await ctx.send("This channel is Family Friendly, you horny.")
                        return
                    
                submissions = self.reddit.subreddit(chosen_subreddit).top(time_filter='month')
                post_to_pick = random.randint(1,100)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                title = submission.title
                if submission.over_18:
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Go to horny jail.")
                        return
                await ctx.send("*From %s*" % chosen_subreddit)
                await ctx.send(f'**{title}**')
                await ctx.send(submission.url)
                

                
                    

            else:
                await ctx.send("Crystal Braves....")

    @commands.command()
    async def addsub(self, ctx, *, message):
        message = message.lower()
        if message not in REDDIT_SUBREDDITS:
            REDDIT_SUBREDDITS.append(message)
            await ctx.send("The subreddit %s has been added to my library." % message)
        else:
            await ctx.send("I already know that subreddit, I even moderate it.")

    @commands.command()
    async def subs(self, ctx):
        await ctx.send("These are the subreddits I frequently visit: " % ", ".join(REDDIT_SUBREDDITS))

    @commands.command(brief="Random picture of a cat")
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:   
                    data = await r.json()

                    embed = discord.Embed(title="Meow")
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat")

                    await ctx.send(embed=embed)

    @commands.command(brief="Random picture of a dog")
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://random.dog/woof.json") as r:   
                    data = await r.json()

                    embed = discord.Embed(title="Woof")
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="http://random.dog")

                    await ctx.send(embed=embed)
    @commands.command(brief="kekw")
    async def kekw(self,ctx):
        with open('./data/my_image.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.channel.send(file=picture)
    
    @commands.command(brief="Random xkcd")
    async def x (self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with  cs.get("https://xkcd.com/info.0.json") as r:
                    data = await r.json()
                    last = data["num"] - 1
                    pick = random.randint(1, last)
                x = f"https://xkcd.com/{pick}/info.0.json"
                async with  cs.get(x) as r:
                    data = await r.json()

                    embed = discord.Embed(title=data["title"])
                    embed.set_image(url=data["img"])
                    embed.set_footer(text=data["alt"])

                    await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Images(bot))