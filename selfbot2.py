import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot (command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def draw(ctx):
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    await ctx.send(random.choice(emodji))
@bot.command()
async def halo(ctx):
    await ctx.send("Hi selamat datang!")
@bot.command()
async def bye(ctx):
    await ctx.send("dadah hati-hati")
@bot.command()
async def password(ctx, pass_length = 8):
    await ctx.send(gen_pass(pass_length))

bot.run("")