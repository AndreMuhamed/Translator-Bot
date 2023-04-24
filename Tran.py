import discord
from googletrans import Translator

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!translate'):
        translator = Translator()
        try:
            text = message.content.split(' ', 1)[1]
            translated = translator.translate(text)
            await message.channel.send(f'Translation: {translated.text}')
        except:
            await message.channel.send('Please provide text to translate.')

bot.run('TOKEN')
