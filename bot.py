import time
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer
bot = commands.Bot('.')
bot.remove_command('help')
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 300','options': '-vn'}

# Definições:
Voice_Soba_Id = 1049168326586286100 # Aqui você insere o ID da sala de voz onde deseja que o bot esteja.
Link_Radio_Stanice = 'http://192.168.2.13:5006/listen/braixens_radio/radio.mp3' #Oentre no link da estação de rádio online aqui.

@bot.event
async def on_ready():
    LinkRadia = discord.FFmpegPCMAudio(Link_Radio_Stanice,**FFMPEG_OPTIONS)
    vc = await bot.get_channel(Voice_Soba_Id).connect()
    vc.play(LinkRadia)
    print(bot.user)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"Braixen's Radio - {['title']}")) #atualiza o status do bot

bot.run('seu_lindo_Token_Aqui') #seu token
