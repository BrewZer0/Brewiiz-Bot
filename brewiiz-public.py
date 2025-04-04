import discord
from discord.ext import commands
import io
import os
import logging

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.messages= True
intents.message_content = True
allowed_mentions = discord.AllowedMentions(everyone = True)
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.command()
async def sxe(ctx):
	"""
    From RobotLiberaBot's code.
    """

	await ctx.send('[came here to share this video](https://youtu.be/2SdGkkp1aq8)')
    

@bot.command()
async def formattest(ctx):
	"""
    Discord Formatting Tests
    """

	await ctx.send('# THIS IS HEADER\n ## THIS IS HEADER 2\n### THIS IS HEADER 3\n**THIS IS BOLD TEXT**\n*THIS IS ITALICIZIED(?)TEXT*\nTHIS IS NORMAL TEXT\n`this is code block 1`\n ``this is code block 2``\n```this is code block 3```\n ~~strikethrough~~\n-# Shmol.')
  
       
@bot.command()
async def todo(ctx):
	await ctx.send('to do:\n- add linux commands:\n- try suggestions for it')

@bot.command()
async def calc(ctx, *, expression: str):
    """
    calculate some mathematical expressions.
    """
    try:
        # Special exception for "9 + 10"
        if expression.strip() == "9 + 10":
           
            await ctx.send("[uhm](https://files.catbox.moe/utoj1g.mp4)")
            return

        # Replace any commas with dots for decimal points
        expression = expression.replace(',', '.')
        
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        
        # Send the result back to the user
        await ctx.send(f"```{result}```\nYou Typed {expression}.")
    
    except Exception as e:
        # Send an error message if the evaluation fails
        await ctx.send(f"Error in calculation: {e}")

@bot.command()
async def uname(ctx):
            """
  Throws Linux Kernel, Hostname and so on
    """

            comd = os.popen("uname -a").read()
            comd.replace("`", "\\`")
            
            printer = f"```\n{comd}\n```"
            await ctx.send(printer)

@bot.command()
async def pwd(ctx):
            comds = os.popen("pwd").read()
            comds.replace("`", "\\`")
            
            printer = f"```\n{comds}\n```"
            await ctx.send(printer)     
 
@bot.command()
async def fetch(ctx):
            comds = os.popen("sh /path/to/POSIX/fetch.sh").read()
            comds.replace("`", "\\`")
            
            printer = f"```\n{comds}\n```"
            await ctx.send(printer)     
            
@bot.command()
async def date(ctx):
            comds = os.popen("date").read()
            comds.replace("`", "\\`")
            
            printer = f"it's {comds}"
            await ctx.send(printer)    
 
            printer = f"{comds}"
            await ctx.send(printer)   
@bot.command()
async def presents(ctx):
         await ctx.send("**Hi, i'm Brewiiz, a bot coded in discord.py.**\n i was originally a thousand different things, starting from robot liberabot (viznut, you're the fucking goat of demos) back in i guess january 2025. i forgor 💀\n\nSlightly based from **Buck's BrewBot code** which solved my whole issue with embedding GNU/Linux commands to linux for shits and giggles (as simple as an os.popen statement, almost).\n i will expand to add more functionalities from other bots, such as an image to ASCII converter. Hope you use me as i upgrade and... contribute if you can code with discord.py.\nComing soon to a github near you :3\n-# Brewiiz PFP by <@1300105674285387898>. ")         

bot.run('ADD_A_TOKEN')
