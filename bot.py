from dotenv import load_dotenv
from pathlib import Path
import os

import discord
from discord.ext import commands

# fetch environment variables from .env file
env_path = Path('.env')
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')

# run the bot
client = commands.Bot(command_prefix='~~')

'''
EVENTS
1. Check whether bot is ready/online
2. Delete messages with "bad words"
3. Return on command error
'''

@client.event
async def on_ready():
    print('i, meme-a-tron-2000, am online 🤖!')

# automatic moderation
f1 = open('./commands/bad_words.txt', 'r')
bw = f1.readlines()

bad_words = []
for i in range(len(bw)):
    bad_words.append(bw[i].replace("\n", ""))

@client.event
async def on_message(msg):
    for word in bad_words:
        if word in msg.content.lower():
            await msg.delete()
            # await ctx.send('your message got deleted because it contained an nsfw word. 🤫🤫🤫')

    await client.process_commands(msg)

# command error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("oops! you can't do that 🤡")
        await ctx.message.delete()

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("seems like you forgot to enter the extra information required 😞 pls try again")
        await ctx.message.delete()

    else:
        raise error

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
2. User Information
3. Clear Messages
4. Kick Members
5. Ban Members
6. Unban Members
7. Mute Members
'''

# SERVER RULES
f2 = open('./commands/rules.txt', 'r')
rules = f2.readlines()

@client.command(aliases=['rules'])
async def rule(ctx, *, num):
    await ctx.send(rules[int(num) - 1])

# USER INFORMATION
@client.command(aliases=['user', 'info', 'whomst'])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member:discord.Member):
    embed = discord.Embed(title=member.name, description=member.mention, color=discord.Colour.blue())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'requested by { ctx.author.name }')
    await ctx.send(embed=embed)

# CLEAR MESSAGES
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True) # can only be done if you have permission to manage messages on this server
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

# KICK MEMBERS
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason='no reason provided :/'):
    try:
        await member.send(f'{{}} has been kicked from this community, because {{}}'.format(member.name, reason))
    except:
        await ctx.send(f'oops! it seems like {{}} has closed their dms'.format(member.name))
    await member.kick(reason=reason)

# BAN MEMBERS
@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason='no reason provided :/'):
    try:
        await member.send(f'{{}} has been banned from this community, because {{}}'.format(member.name, reason))
    except:
        await ctx.send(f'oops! it seems like {{}} has closed their dms'.format(member.name))
    await member.ban(reason=reason)

# UNBAN MEMBERS
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member:discord.Member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discrimiator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(f'{{}} has been unbanned!'.format(member_name))
            return

    await ctx.send(f"{{}} wasn't found :(".format(member))

# MUTE MEMBERS
@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member:discord.Member):
    muted_role = ctx.guild.get_role(CLIENT_ID)

    await member.add_roles(muted_role)
    await ctx.send(f'{{}} has been muted'.format(member.mention))

# close all open files
f1.close()
f2.close()

# run the bot
client.run(TOKEN)