import discord

TOKEN =
CHANNELID =

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