import discord, random, weather_app

# basecode taken from discord.py documentation, modded for personal use. 
# will be changed when i have time to be flexible in implementation :)
# https://discordpy.readthedocs.io/en/stable/quickstart.html

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
CLIENT_KEY_HERE = ''

prefix = ''
announceChannel = None # fill in for idea

stupid_questions = {
    'do it itch?',
    'Where are you right now',
    'do you smoke weed',
    'The game. You have lost it',
    'post pictures of your houses',
    'do you be throwin it back',
    'who up playing with they worm',
    'is anyone else #Nodding right now???',
    'Burgjer'
}

@client.event
async def on_ready():
    print(f'Bot has logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #choose cmd
    if message.content.startswith('$choose'):
        choiceMsg = message.content[7:]
        choices = choiceMsg.split(' | ')
        await message.channel.send(choices[random.randrange(len(choices))])

    if message.content.startswith('$roll'):
        afterMessage = message.content[5:]
        post = afterMessage.split(' ')

        rollVal = 100
        if (len(post) > 1):
            if post[1].isdigit():
                rollVal = int(post[1])

        rolled = random.randrange(rollVal+1)
        if bool(dubsCheck(rolled)) or (rolled == 100):
            messg = '**holy fucking bingle,** ' + message.author.name + ' rolled: ' + str(rolled)
            await message.channel.send(messg)
        else:
            messg = message.author.name + ' rolled: ' + str(rolled)
            await message.channel.send(messg)
    
    if message.content.startswith('$weather'):
        afterMessage = message.content[8:]
        if len(afterMessage) > 1:
            weather = weather_app.getweather(afterMessage[1])
            for vals in weather.items():
                await message.channel.send() #TODO: combine all into one string, using 'keys: item\n'
        else:
            await message.channel.send('**ERROR:** Did not detect weather location data! Please try again.')

# basic idea ripped from g4g
# https://www.geeksforgeeks.org/check-if-all-the-digits-of-the-given-number-are-same/

def dubsCheck(n):
    lastDig = n % 10
    dubbable = False
    if n > 10:
        dubbable = True
    while (n != 0):
        curr = n % 10
        n = n // 10
        if (curr != lastDig):
            return False
    return True and dubbable


client.run(CLIENT_KEY_HERE)