import discord
import random
from discord.ext import commands

# client holds instance of bot and we can use a different var tbh
client = commands.Bot(command_prefix='.')


@client.event
# When everything's ready the bot puts itself into ready state
async def on_ready():
    print('Bot is ready.')


# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')


# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left a server.')

# ctx = context or something - look in documentation
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# All the strings in the list can run the command aka we don't need _8ball


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain,',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes-definitely.',
                 'You may rely on it,',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

# Token is from Discord Developer Portal -> Bot and keep this safe (key)
client.run("YOUR KEY")
