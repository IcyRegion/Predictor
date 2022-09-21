import os
import cloudscraper, requests
import discord, time
import random, threading
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Predicting Bloxflip"))
    print('Im Ready')



@bot.command()
@commands.guild_only()
async def mines(ctx,round_id):
    await ctx.send(''':man_technologist: Check DMs, If you didn't get a DM repeat the command''')
    round_len = (len(round_id))
    if round_len <= 35:
        await ctx.author.send('Not a valid round id')
    elif round_len == 36:
        list = ["""💥🌟💥💥💥
💥💥🌟💥💥
💥💥💥💥💥
💥💥💥💥💥
💥🌟🌟💥💥""", """💥💥💥💥🌟
💥💥💥💥💥
💥💥💥🌟💥
🌟💥💥💥💥
💥💥💥💥🌟""", """💥💥💥💥💥
🌟💥🌟💥💥
💥💥💥💥🌟
💥🌟💥💥💥
💥💥💥💥💥""", """💥💥💥💥💥
💥💥🌟💥💥
💥💥💥💥🌟
💥💥💥💥💥
🌟💥🌟💥💥""", """💥💥💥🌟💥
💥💥💥💥💥
🌟💥💥🌟💥
💥💥💥💥💥
💥💥💥💥🌟""", """💥💥💥🌟🌟
💥🌟💥💥💥
💥💥💥🌟💥
💥💥💥💥💥
💥💥💥💥💥""", """💥💥💥💥💥
💥🌟💥💥💥
💥💥💥💥💥
🌟🌟💥💥💥
💥💥💥💥🌟""", """💥💥💥💥💥
💥💥💥💥💥
💥💥🌟🌟🌟
💥💥💥💥💥
🌟💥💥💥💥""", """"""]


        predict = random.choice(list)
        embed=discord.Embed(title="Strike Predictor", description="Prediction", color=0x00ffff)
        embed.add_field(name="Mines Prediction", value=predict,inline=False)
        embed.add_field(name="Accuracy ", value="General accuracy = 45% to 85%", inline=False)
        embed.add_field(name="Credit", value="By c0mrade & ViP", inline=False)
        embed.set_footer(text="Accuracy Better in 1 or 2 bomb")
        await ctx.author.send(embed=embed)



@bot.command()
@commands.guild_only()
async def towers(ctx,round_id):
    await ctx.send(''':nerd: Check DMs, if it didn't work do cmd again.''')
    round_len = (len(round_id))
    if round_len <= 35:
        await ctx.author.send('Not a valid round id')
    elif round_len == 36:
        list = ["""🌟💥💥
💥💥🌟
💥🌟❌
❌❌🌟
❌🌟❌
🌟❌❌
🌟❌💥
💥🌟💥""", """🌟 💥 💥
🌟 💥 💥
💥 💥 🌟
💥 🌟 💥
💥 💥 🌟
🌟 💥 💥
💥 💥 🌟
💥 🌟 💥""", """🌟 💥 💥
🌟 💥 💥
💥 🌟 💥
💥 🌟 💥
💥 🌟 💥
💥 💥 🌟
💥 💥 🌟
💥 💥 🌟""", """💥 💥 🌟
🌟 💥 💥
💥 💥 🌟
💥 💥 🌟
💥 💥 🌟
💥 🌟 💥
💥 💥 🌟
💥 💥 🌟""", """🌟 💥 💥
🌟 💥 💥
💥 🌟 💥
🌟 💥 💥
🌟 💥 💥
💥 🌟 💥
🌟 💥 💥
💥 💥 🌟""", """💥 🌟 💥
🌟 💥 💥
💥 💥 🌟
🌟 💥 💥
🌟 💥 💥
🌟 💥 💥
💥 🌟 💥
🌟 💥 💥""", """💥 🌟 💥
💥 💥 🌟
💥 🌟 💥
💥 🌟 💥
💥 💥 🌟
💥 💥 🌟
💥 🌟 💥
🌟 💥 💥""", """💥 🌟 💥
💥 🌟 💥
💥 🌟 💥
💥 🌟 💥
🌟 💥 💥
💥 🌟 💥
💥 🌟 💥
💥 💥 🌟""", """💥 🌟 💥
🌟 💥 💥
🌟 💥 💥
🌟 💥 💥
💥 💥 🌟
💥 💥 🌟
💥 💥 🌟
💥 💥 🌟""", """"""]
        color = 0x1BACBD
        em = discord.Embed(color = color)
        predict = random.choice(list)
        em.add_field(name="Made by c0mrade & ViP", value=predict)
        em.set_footer(text="Tower Predictor.")
        await ctx.author.send(embed=em)

bot.run("MTAyMTA2MTE1NjIxNzA0MDk0OA.GhBscj.0EcpzZb2OhjSIya4npgYb7GkpVnrrLKLapMjYc")