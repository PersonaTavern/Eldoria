# main.py
# Import modules and libraries 
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Get Environment Variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Enable intents
intents = discord.Intents.default()
intents.guilds = True  # Enables GUILDS intent, which includes message_content

# Configure bot
bot = discord.Client()
bot = commands.Bot(command_prefix='eh~ ')

@bot.event
async def on_ready():
   print("Eek-Hue ready!")
	
@bot.event
async def on_message(message):
    # Process commands
    await bot.process_commands(message)

    # Respond to "hello" (case-insensitive)
    if message.content.lower() == "hello":
        await message.channel.send("hey dirtbag")

## Reference for listensers
"""
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
"""

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(DISCORD_TOKEN) 
