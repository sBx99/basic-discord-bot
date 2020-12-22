from dotenv import load_dotenv
from pathlib import Path
import os

import discord
from discord.ext import commands

# fetch token from .env file
env_path = Path('.env')
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('TOKEN')

# run the bot
client = commands.Bot(command_prefix='~')

@client.event
async def on_ready():
    print('i, meme-a-tron-2000, am ready 🤖!')

# COMMANDS
# ctx == context

'''
INTRODUCTORY COMMANDS
1. Welcome/Introduction Nessage
2. Help Command
'''

# INTRODUCTION
@client.command(aliases=['hello', 'hi'])
async def hey(ctx):
    await ctx.send('hey there! i am meme-a-tron-2000, at your service with some freshly generated memes!')

# HELP
@client.command(aliases=['pls'])
async def helpme(ctx):
    await ctx.send('these are the commands you can use: \n')

'''
MODERATION COMMANDS
1. Server Rules
2. Clear Messages
3. Kick Members
4. Ban Members
5. Unban Members
'''

# SERVER RULES
f = open('./commands/rules.txt', 'r')
rules = f.readlines()

@client.command(aliases=['rules'])
async def rule(ctx, *, num):
    await ctx.send(rules[int(num) - 1])

# CLEAR MESSAGES
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True) # can only be done if you have permission to manage messages on this server
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

# KICK MEMBERS
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason='no reason provided :/'):
    await member.send(f'{{}} has been kicked from this community, because {{}}'.format(member.name, reason))
    await member.kick(reason=reason)

# BAN MEMBERS
@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason='no reason provided :/'):
    await member.send(f'{{}} has been banned from this community, because {{}}'.format(member.name, reason))
    await member.ban(reason=reason)

# UNBAN MEMBERS

client.run(TOKEN)