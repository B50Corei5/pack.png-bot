import discord
import json
import logging
import inspect
import re
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('^'), description='Answering pack.png questions!') # sets the prefix+description of the bot

bot.remove_command("help") # removes the help command because its not needed and the default one sucks

def FAQMessage_factory(bot, names, regexes, channel_whitelist, message):
    """return cog classes, needed for cog name"""
    
    class FAQMessage(commands.Cog, name=names[0]):
        def __init__(self, bot, names, regexes, channel_whitelist, message,):
            self.bot = bot
            self.names = names
            self.command = commands.command(names[0], aliases=names[1:])(self.send) # create the command to be later added to the bot
            self.message = message
            self.regexes = [re.compile(reg) for reg in regexes]
            self.channel_whitelist = channel_whitelist

        @commands.Cog.listener()
        async def on_message(self, message):
            if message.author.id != self.bot.user.id: # check for the bot beign the author
                if message.channel.id in self.channel_whitelist:# check for channel in channel_whitelist
                    if any(r.match(message.content) for r in self.regexes): # check if any of the regexes are matched
                        await self.send(message.channel) # send the message using the method below

        async def send(self, channel): # this is a seperate method because of the command
            await channel.send(self.message) # simply send the message

    return FAQMessage(bot, names, regexes, channel_whitelist, message)

channels = [666575359411748875, 666758275504537604, 666813360867770388, 660701994549379125]

faq_messages = [
    FAQMessage_factory(bot, ["dream", "dreams"], [r"dream.?s?.?method",], channels, "Hey, it looks like you mentioned Dream! Unfortunately we cannot use that method because we don't have enough information. But here's some other ideas: {link to a google doc}"),
    FAQMessage_factory(bot, ["theseed",], [r"seed.is"], channels, "Hey, it looks like you mentioned what the seed is! If you actually found the seed, please message a mod. If you're saying this as a joke, please dont :)")
    # FAQMessage(bot, ["",], [r""], channels, "Hey, it looks like you mentioned trying a seed or method! There's lots of good information on https://packpng.com/faq and in ANNOUNCEMENTS CHANNEL")
    # FAQMessage(bot, ["",], [r""], channels, "Hey, it looks like you mentioned supercomputer! Thankfully " + '<@459235187469975572>' + " is dedicating several supercomputers towards this!")
    # FAQMessage(bot, ["",], [r""], channels, "Hey, it looks like you mentioned a quantum computer! Unfortunately this won't help with this problem and we already have enough computing power")
    # FAQMessage(bot, ["",], [r""], channels, "Hey, it looks like you mentioned supercomputer! Thankfully " + '<@459235187469975572>' + " is dedicating several supercomputers towards this!")
    # FAQMessage(bot, ["",], [r""], channels, "Hey, it looks like you mentioned a quantum computer! Unfortunately this won't help with this problem and we already have enough computing power")
]


@bot.event 
async def on_ready(): # after everything is done and stuff get ready to login and respond to gentards
    await bot.change_presence(activity=discord.Game(name='responding to pack.png questions', type=0, url='https://packpng.com/faq')) # sets description and stuff
    logging.info('Logged in as:{0} (ID: {0.id})'.format(bot.user)) # to console
    for faq in faq_messages:
        bot.add_cog(faq)
        bot.add_command(faq.command)

with open('auth.json') as data_file: # opens auth.json so i dont have the tokens in this file
    auth = json.load(data_file) # loads the json

bot.run(auth['token']) # login

