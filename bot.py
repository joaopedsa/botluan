import discord
import time
from discord.ext import commands

Client = discord.Client()
bot_prefix = "."
bot = commands.Bot(command_prefix=bot_prefix)


@bot.event
async def on_ready():
    print("Ligado")
    await bot.change_presence(game=discord.Game(name='Merda na Cara'))


@bot.command(pass_context=True)
async def amigo(ctx):
    await bot.say("MEU AMIGO!")


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("TA MEIO RUIM PQ TA RENDENRIZANDO")
@bot.command(pass_context=True)
async def bugabuga(ctx):
    await bot.say("+rule34 overwatch")

@bot.command(pass_context=True)
async def baule(ctx):
    await bot.say("Supino Preto")


@bot.command(pass_context=True)
async def davijones(ctx):
    await bot.say("GRANDE HOMEM")
@bot.command(pass_context=True)
async def scariot(ctx):
    await bot.send_file(ctx.message.channel,'scariot.png')

@bot.command(pass_context=True)
async def nani(ctx):
    try:
        voice = conecta(ctx)
        player = await voice.create_ytdl_player('https://youtu.be/jwAxc56Xz_c')
        player.start()
    except:
        bot.say("Entre em um canal de voz")
@bot.command(pass_context=True)
async def falaluan(ctx):
    try:
        voice = await bot.join_voice_channel(ctx.message.author.voice_channel)
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=qjjT960FYt4')
        player.start()
    except:
        bot.say("Entre em um canal de voz")
@bot.command(pass_context=True)
async def briga(ctx):
    await bot.say("pls meme")
    time.sleep(5)
    await bot.say("ARREGO")

@bot.event
async def on_message(message):
    if message.content.startswith('Joao Pedro Santana'):
        await bot.send_message(message.channel,'homem mais delicioso do mundo')
        await bot.wait_for_message(author=message.author,content='s2')
        await bot.send_message(message.channel,'s2')
    elif message.content.startswith('pls meme'):
        await bot.send_message(message.channel, 'Sapão Filho Da Puta')
    elif message.content.startswith('faço computação'):
        await bot.send_file(message.channel,'shitlife.png')
    elif message.content.startswith('bot fdp'):
        await bot.send_message(message.author,"seu merda")
        await bot.send_file(message.author, "cancianfdp.png")
        await bot.send_message(message.author,'s2')
        await bot.wait_for_message(author=message.author, content='s2')
        await bot.send_message(message.author, 's2')
    elif message.content.startswith('suco'):
        await bot.send_file(message.channel,'suco.png')
    await bot.process_commands(message)

bot.run("MzUxMDU5Njk2NzUwNDI4MTYw.DINFsg.OwkUmbqfPmzbx4KGgEYHRS43qYo")