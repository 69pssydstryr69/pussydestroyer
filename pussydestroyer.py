import discord
import os

bot = discord.Client()

@bot.event
async def on_ready():
    print('motherdie')
    
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if msg.content.startswith('fuck'):
        await msg.channel.send('yourmother')

bot.run(os.environ['TOKEN'])

