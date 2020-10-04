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
	
	#await bot.change_presence(status = discord.Status.online, activity = discord.Game('Чёрную Метку'))
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="стрим Санчиза"))
 
bot.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')

@bot.event
async def on_member_join(member):
    server = member.guild.default_channel
    fmt = 'Welcome to the {1.name} Discord server, {0.mention}, please read the 
    rules and enjoy your stay.'
    await bot.send_message(server, fmt.format(member, member.guild))

@bot.event
async def on_member_remove(member):
    server = member.guild.default_channel
    fmt = '{0.mention} has left/been kicked from the server.'
    await bot.send_message(server, fmt.format(member, member.guild))
