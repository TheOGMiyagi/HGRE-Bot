# <--- IMPORTS --->
import os                                                # IMPORT THE OS MODULE.
import asyncio                                           # IMPORT THE ASYNC INPUT/OUTPUT
from dotenv import load_dotenv                           # IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
load_dotenv()                                            # LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.

import discord                                           # IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from discord.ext import commands                         # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext.commands import client                  # IMPORT CLIENT FROM DISCORD.EXT.COMMANDS

import tribute                                           #? TRIBUTE MODULE
import tribute_db                                        #? TRIBUTE DATABASE MODULE
from tribute_db import Tribute_Database as Database      #? DATABASE OBJECT w/ ALIAS("Database")

# <--- GLOBAL VARIABLES --->
# with open('config.json') as file
    # Settings = json.load(file)
    # Prefix = Settings['Prefix']
client = commands.client(command_prefix="hg!")
Token = os.environ['TEST_TOKEN']

def main():
    client.run(Token)

# DRIVER CODE
if __name__ == "__main__":
    main()
    input("Press Enter To Exit.") #? This is added to keep the script from exiting after the logic is ran.
else:
    print(f"{__name__} was successfully imported.")
