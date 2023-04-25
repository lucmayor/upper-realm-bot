import discord, random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
CLIENT_KEY_HERE = ''

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

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
        if post[0].isdigit():
            print(f'this has worked, new value: ' + str(int(post[0])))
            rollVal = int(post[0])

        rolled = random.randrange(rollVal+1)
        if ((rolled % 11) == 0) or (rolled == 100):
            messg = 'holy fucking bingle, ' + message.author.name + ' rolled: ' + str(rolled)
            await message.channel.send(messg)
        else:
            messg = message.author.name + ' rolled: ' + str(rolled)
            await message.channel.send(messg)


client.run(CLIENT_KEY_HERE)