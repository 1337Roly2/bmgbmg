import discord
 
from discord.ext import commands, tasks
from text_bot import TextBot
from itertools import cycle
import datetime
 
client = commands.Bot(command_prefix = '!')

status = cycle(['стрим Санчиза','аккаунты на FunPay','стрим Пахана','стрим Стила','канал #about-us','стрим Эскобарова','за блоком']) 
client.add_cog(TextBot(client))

@client.event
async def on_ready():
	change_status.start()
	print('Logged in as:\n{0} (ID: {0.id})'.format(client.user))
	       
@tasks.loop(seconds=60)
async def change_status():
	await client.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=(next(status))))

@client.event
async def on_member_join(member):
	print(f'{member} joined.')

@client.event
async def on_member_remove(member):
	print(f'{member} left.')
     
@client.command(pass_contex = True)
async def emb(ctx):
	channel = ctx.message.channel
	embed = discord.Embed(
		title = 'Title',
		description = 'Lorem Ipsum asdasd',
		colour = discord.Colour.black()
	)
	
	# embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
	await client.send_message(channel, embed=embed)


client.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')
