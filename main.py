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

@client.commands()
async def emb(ctx):
	embed=discord.Embed()
	embed.add_field(name="undefined", value="undefined", inline=False)
	await self.client.say(embed=embed)
	
	
client.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')
