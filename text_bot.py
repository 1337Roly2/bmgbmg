from discord.ext import commands
from discord.utils import get
 
words = ['чм','метка','black','mark','gang','чёрн','черн','legen','легенд','bmg']

 
class TextBot(commands.Cog):
 
    def __init__(self, bot):
        self.bot = bot
 
    @commands.Cog.listener()
    async def on_message(self, ctx):
        """ Emoji reacts to someone who says"""
        if ctx.author == self.bot.user:
            return
 
        if (any(st in ctx.content.lower() for st in words)):
 
            await ctx.add_reaction(get(self.bot.emojis, name='bmg')) 
            await ctx.add_reaction(get(self.bot.emojis, name='c1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='e1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='r1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='n1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='a1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='ya')) 
            await ctx.add_reaction(get(self.bot.emojis, name='probel')) 
            await ctx.add_reaction(get(self.bot.emojis, name='m1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='e2')) 
            await ctx.add_reaction(get(self.bot.emojis, name='t1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='k1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='a2')) 
            await ctx.add_reaction(get(self.bot.emojis, name='bmg2')) 
            #await ctx.add_reaction('👀')
            await self.bot.process_commands(ctx)
            
