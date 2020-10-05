import discord
 
from discord.ext import commands, tasks
from text_bot import TextBot
 
client = commands.Bot(command_prefix = '.')



client.add_cog(TextBot(client))
 
@client.event
async def on_ready():
	print('Logged in as:\n{0} (ID: {0.id})'.format(client.user))

@client.command(pass_context=True)
async def join(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await client.join_voice_channel(channel)


client.run('NjU5NzQ2MjkyNjgzMTEyNDU4.XgSynQ.F7zmQnNuJfmTlIIMLRHO87N8MqQ')
