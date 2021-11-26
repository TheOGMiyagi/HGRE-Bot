"""
Description:
This Cog contains all the events and commands related to administration and administrator tools.
"""
# IMPORTS
#import [Module/Package]
import discord                          # IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.

class Admin_Tools(commands.Cog):
    def __init__(self, client):
        """Initializes the cog, passing in a client to associate itself with."""
        self.client = client
    
    # <--- Purge Messages --->
    @commands.command(name="purge", aliases=["clear", "Purge", "Clear"])
    @commands.has_permissions(manage_messages=True)
    async def purge(ctx, amount: int=5):
        channel = ctx.message.channel
        messages = []
        async for msg in commands.logs_from(channel, limit=amount):
            messages.append(msg)
        await commands.delete_messages(messages)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
    @purge.error
    async def purge_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Error - **{ctx.message.author.display_name}** does not have **Manage Messages** Permissions.")
    
    # <--- Userinfo Command --->
    @commands.command(name="userInfo", aliases=["uInfo", "Uinfo"])
    @commands.has_permissions(administrator=True)
    async def userinfo(ctx, user: discord.Member):
        # ? Unimplemented Try-Catch Error Handling
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
def setup(client):
    """Adds The Cog To The Client."""
    client.add_cog(Admin_Tools(client))