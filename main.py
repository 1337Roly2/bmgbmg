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
    server = member.guild
    channel = guild.default_channel
    retStr = str("""```yaml\nПривет!\nДобро пожаловать на наш сервер!\nНадеюсь тебе тут понравится.\nЕсли заблудешься пиши !help,кстати у нас все команды пишутся с !\nДля получения роли зайди в чат получения роли\nудачи тебе```""")
    embed = discord.Embed(title="Welcome",colour=discord.Colour.blue())
    embed.add_field(name="Привет",value=retStr)
    await bot.send_message(channel, embed=embed)
