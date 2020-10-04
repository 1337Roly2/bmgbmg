import discord
 
from discord.ext import commands, tasks
from text_bot import TextBot
from itertools import cycle
 
client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))


status = cycle(['стрим Санчиза','аккаунты на FunPay','стрим Пахана','стрим Стила','канал #about-us','стрим Эскобарова','за блоком']) 
client.add_cog(TextBot(client))
 
@client.event
async def on_ready():
	change_status.start()
	print('Logged in as:\n{0} (ID: {0.id})'.format(client.user))

@client.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	awiat client.join_voice_channel(channel)


@tasks.loop(seconds=60)
async def change_status():
	await client.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=(next(status))))



@client.event
async def on_member_join(member):
	print(f'{member} joined.')

@client.event
async def on_member_remove(member):
	print(f'{member} left.')

client.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')
