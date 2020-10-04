import discord
 
from discord.ext import commands, tasks
from text_bot import TextBot
from itertools import cycle
 
bot = commands.Bot(
	command_prefix=commands.when_mentioned_or('!'),
	description='BOT'
)
status = cycle(['стрим Санчиза','стрим Пахана']) 
bot.add_cog(TextBot(bot))
 
@bot.event
async def on_ready():
	change_status.start()
	print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
	       
@tasks.loop(seconds=3)
async def change_status():
	await bot.change_presence(status = discord.Status.online, activity = discord.Game(next(status)))
	#await bot.change_presence(activity=discord.watching(next(status)))

@bot.event
async def on_member_join(member):
	print(f'{member} joined.')

@bot.event
async def on_member_remove(member):
	print(f'{member} left.')
	      
	
	
bot.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')
