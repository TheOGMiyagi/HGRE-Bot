# <--- IMPORTS --->
import os                               # IMPORT THE OS MODULE.
import asyncio                          # IMPORT THE ASYNC INPUT/OUTPUT
from dotenv import load_dotenv          # IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
load_dotenv()                           # LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.

import discord                          # IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext.commands import Bot    # IMPORT BOT FROM DISCORD.EXT.COMMANDS

import xdice                            # IMPORT XDICE LIBRARY
import json                             # IMPORT THE JSON MODULE
 

# <--- GLOBAL VARIABLES --->
# with open('config.json') as file
    # Settings = json.load(file)
    # Prefix = Settings['Prefix']
bot = commands.Bot(command_prefix="hg!")
Token = os.environ['DISCORD_TOKEN']
Guild = os.environ['DISCORD_GUILD']
Dice_Channels_TEST = os.environ['DICE_CHANNEL_ID_ONE']
Dice_Channels_TBS = os.environ['DICE_CHANNEL_ID_TWO']
Dice_Channel = os.environ['DICE_CHANNEL_ID_THREE']


# <---- Removes Built-In Help Command --->
bot.remove_command('help')


# <--- Console Ready --->
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == Guild:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    


# <--- Commands --->
@bot.command(name="help", aliases=["h", "Help", "H"])
async def help(ctx):
    embed = discord.Embed(title="HGRE Bot Help", description="Here is all of the commands for HGRE Bot!", color=0x0072ff)
    embed.add_field(name="Information Commands", value="hg!ping - Ping Pong!\nhg!userinfo @user - Shows you info about the user!\nhg!serverinfo - Shows you info about the server!")
    embed.add_field(name="Dice Commands", value="hg!roll - Roll The Dice")
    embed.set_footer(text="HGRE Bot by TheOGMiyagi")
    await ctx.message.channel.send(embed=embed)

# <--- Ping --->
@bot.command(name="ping", aliases=["Ping"])
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:", description="", color=0x0072ff)
    embed.set_footer(text="HGRE Bot by TheOGMiyagi")
    await ctx.message.channel.send(embed=embed)
    
# <--- Userinfo Command --->
@bot.command(name="userInfo", aliases=["uInfo", "Uinfo"])
async def userinfo(ctx, user: discord.Member):
    # try:
        # if user = None:
            # raise Exception("No User Specified.")
        embed = discord.Embed(title="{}'s Info".format(user.name), description="Here's What I could Find in Discord's Database!", color=0x0072ff)
        embed.add_field(name="Name", value=user.name)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Role", value=user.top_role, inline=True)
        embed.add_field(name="Joined At", value=user.joined_at, inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="HGRE Bot by TheOGMiyagi")
        await ctx.message.channel.send(embed=embed)
    # except Exception as error:
        # print(error)
        # await ctx.message.channel.send("Please Specify A User.")

# <--- Server Info Command --->
@bot.command(name="serverInfo", aliases=["sInfo", "Sinfo"])
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s Server Info".format(ctx.message.guild.name), description="Here's What I could Find in Discord's Database!", color=0x0072ff)
    embed.add_field(name="Server Name", value=ctx.message.guild.name)
    embed.add_field(name="ID", value=ctx.message.guild.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.guild.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.guild.members))
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    embed.set_footer(text="HGRE Bot by TheOGMiyagi")
    await ctx.message.channel.send(embed=embed)

# <--- Roll --->
@bot.command(name="roll", aliases=["r", "Roll", "R"])
async def roll(ctx,diceExpression="1d20"):
        channel_id = ctx.message.channel.id
        if channel_id != 830170219510366219:
            await ctx.message.channel.send(f"<#{ctx.message.channel.id}> is not authorized for Dice Commands")
        else:
            xdice_pattern = xdice.Pattern(diceExpression)
            results = xdice_pattern.roll()
            embed = discord.Embed(title=f"{ctx.message.author.display_name} Made A Dice Roll", description=f"{ctx.message.author.display_name} rolled: {diceExpression} -> {results}", color=0x0072ff)
            embed.set_footer(text='"May The Odds Be Ever In Your Favor"')
            await ctx.message.channel.send(embed=embed)
    

# <--- Channel ID --->
@bot.command(name="getChannelID", aliases=["channelID", "getChID", "chID"])
async def getChannelID(ctx):
    channel_id = ctx.message.channel.id
    await ctx.message.channel.send(f"<#{channel_id}>'s ID: {channel_id}")

bot.run(Token)