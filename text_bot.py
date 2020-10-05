from discord.ext import commands
from discord.utils import get
 
words = ['чм','метка','блэк','марк','гэнг','нигга','nigga','black','mark','gang','чёрн','черн','legen','леген','bmg','марко']
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

        if (any(st in ctx.content.lower() for st in words2)):
 
            await ctx.add_reaction(get(self.bot.emojis, name='style')) 
            await ctx.add_reaction(get(self.bot.emojis, name='c5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='t5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='i5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='l5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='ya5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='probel')) 
            await ctx.add_reaction(get(self.bot.emojis, name='n5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='e5')) 
            await ctx.add_reaction(get(self.bot.emojis, name='t6')) 
            await ctx.add_reaction(get(self.bot.emojis, name='style2')) 
            #await ctx.add_reaction('👀')
            await self.bot.process_commands(ctx) 
            
            
@client.command()
async def emb(ctx):

	channel = ctx.message.channel
	embed = discord.Embed(
	title='Title',
	description='Lorem Ipsum asdasd',
	colour=discord.Colour.black()
	)
	
	embed.set_author(name='Marco')
	embed.add_field(name='Fueld name', value='Field Name', inline=False)
	# embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
	await ctx.say(embed=embed)
