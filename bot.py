import time
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer
bot = commands.Bot('.')
bot.remove_command('help')
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 300','options': '-vn'}

# Podešavanja:
Voice_Soba_Id = 123456789 # Ovdije upišete ID od voice sobe gdije želite da bot bude.
Link_Radio_Stanice = 'http://balkan.dj.topstream.net:8070/;' #Ovdije upišete link online radio stanice.

@bot.event
async def on_ready():
    LinkRadia = discord.FFmpegPCMAudio(Link_Radio_Stanice,**FFMPEG_OPTIONS)
    vc = await bot.get_channel(Voice_Soba_Id).connect()
    vc.play(LinkRadia)
    print(bot.user)

bot.run('TOKEN') #Vaš token
