import discord
 
from discord.ext import commands
from text_bot import TextBot
 
bot = commands.Bot(
	command_prefix=commands.when_mentioned_or('!'),
	description='BOT'
)
 
bot.add_cog(TextBot(bot))
 
@bot.event
async def on_ready():
	print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
	
	await bot.change_presence(status = discord.Status.online, activity = discord.Status('Чёрную Метку'))
 
bot.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')
