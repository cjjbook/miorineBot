import discord

TOKEN = 'MTE0NDIyNTAzODg5MjAxOTcxMg.GjBDpp.pxu6vpJWWRj7eFyfmRMCARY_qzUIfxYCLuEjT0'
CHANNELID = 915570404205166593

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('봇 가동')

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content == 'hi':
            await message.channel.send('haha')

client.run(TOKEN)