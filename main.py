import discord
 
from discord.ext import commands, tasks
from text_bot import TextBot
from itertools import cycle
from discord.utils import get
import datetime
import os
 
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

@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
	global voice
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)
	
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
	
	await voice.disconnect()
	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
	
@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)
	
	if voice and voice.is_connected():
		await voice.disconnect()

@client.event
async def on_member_join(member):
	for channel in member.guild.channels:
		if str(channel)=="general":
			print('member')
			await client.send_message(f"""Welcome {member.mention}""")


#client.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')
