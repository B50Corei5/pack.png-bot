import discord
import json
import logging
import inspect
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

with open('auth.json') as data_file: # opens auth.json so i dont have the tokens in this file
    auth = json.load(data_file) # loads the json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('^'), description='Answering pack.png questions!') # sets the prefix+description of the bot
bot.remove_command("help") # removes the help command because its not needed and the default one sucks
@bot.event
async def on_message(message): # every time a message is sent in the server
    if message.author.id != 667447141068832768: # prevents bot from going in a loop and responding to itself 
        if message.channel.id == 666575359411748875 or message.channel.id == 666758275504537604 or message.channel.id == 666813360867770388 or message.channel.id == 660701994549379125: # will only do the following if the message is in these channels.
            # if 'word' in message.content.lower():  checks for word in message
            #     await message.channel.send("Hey, it looks like you mentioned word")  responds with this if its found
            if 'dream' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned Dream! Unfortunately we cannot use that method because we don't have enough information. But here's some other ideas: {link to a google doc}")
            if 'have you tried' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned trying a seed or method! There's lots of good information on https://packpng.com/faq and in ANNOUNCEMENTS CHANNEL")
            if 'seed is' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned what the seed is! If you actually found the seed, please message a mod. If you're saying this as a joke, please dont :)")
            if 'have we tried' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned trying a seed or method! There's lots of good information on https://packpng.com/faq and in ANNOUNCEMENTS CHANNEL")
            if 'supercomputer' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned supercomputer! Thankfully " + '<@459235187469975572>' + " is dedicating several supercomputers towards this!")
            if 'quantumcomputer' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned a quantum computer! Unfortunately this won't help with this problem and we already have enough computing power")
            if 'super computer' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned supercomputer! Thankfully " + '<@459235187469975572>' + " is dedicating several supercomputers towards this!")
            if 'quantum computer' in message.content.lower():
                await message.channel.send("Hey, it looks like you mentioned a quantum computer! Unfortunately this won't help with this problem and we already have enough computing power")
            if 'readthepins' in message.content.lower():
                file1 = open("counter.txt", "r+") # opens file
                counter = file1.readline() # reads the line
                counter = int(counter) # str to int
                counter = counter+1 # counter + 1
                counter = str(counter) # int to str
                file1.seek(0) # goes to start of file
                file1.truncate() # yeets the line
                file1.write(counter) # yeets counter back in
                file1.close() # closes the file
                await message.channel.send("PUT SOME FAQ STUFF HERE. this faq has been sent: {0} times.".format(counter)) # sends message with counter. hopefully this makes it ez for people who dont know code what this does

@bot.event 
async def on_ready(): # after everything is done and stuff get ready to login and respond to gentards
    await bot.change_presence(activity=discord.Game(name='responding to pack.png questions', type=0, url='https://packpng.com/faq')) # sets description and stuff
    logging.info('Logged in as:{0} (ID: {0.id})'.format(bot.user)) # to console
bot.run(auth['token']) # login

