from discord.ext import commands
from discord.utils import get
 
words = ['чм','черн','метка','black','mark','gang','чёрная','черный','чёрный','стиль','стил','legen','легенд']
words2 = ['style','стил']   

 
class TextBot(commands.Cog):
 
    def __init__(self, bot):
        self.bot = bot
 
    @commands.Cog.listener()
    async def on_message(self, ctx):
        """ Emoji reacts to someone who says"""
        if ctx.author == self.bot.user:
            return
 
        if (any(st in ctx.content.lower() for st in words)):
 
            await ctx.add_reaction(get(self.bot.emojis, name='c1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='e1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='r1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='n1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='a1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='ya')) 
            await ctx.add_reaction(get(self.bot.emojis, name='bmg')) 
            await ctx.add_reaction(get(self.bot.emojis, name='m1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='e2')) 
            await ctx.add_reaction(get(self.bot.emojis, name='t1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='k1')) 
            await ctx.add_reaction(get(self.bot.emojis, name='a2')) 
            #await ctx.add_reaction('👀')
            await self.bot.process_commands(ctx)
            
             
        if (any(st in ctx.content.lower() for st in words2)):
 
            await ctx.add_reaction(get(self.bot.emojis, name='c5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='t5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='i5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='l5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='ya5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='n5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='e5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='t6')) 
            await ctx.add_reaction(get(self.bot.emojis, name='bmg')) 
            #await ctx.add_reaction('👀')
            await self.bot.process_commands(ctx)
