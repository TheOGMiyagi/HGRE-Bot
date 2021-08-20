"""
Description:
This Cog handles the on-boot operations of the bot (currently loaded but unimplemented).
"""
# IMPORTS
#import [Module/Package]
import discord                          # IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.

class Boot(commands.Cog):
    def __init__(self, client):
        """Initializes the cog, passing in a client to associate itself with."""
        self.client = client
    
def setup(client):
    """Adds The Cog To The Client."""
    client.add_cog(Boot(client))
    