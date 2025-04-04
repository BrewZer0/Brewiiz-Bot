import discord
from discord.ext import commands
import io
import os
import logging
from PIL import Image

print("Brewiiz Bot Runner\n 2025 Brewy. the fuck are rights?")

logging.basicConfig(level=logging.INFO)
intents = discord.Intents.default()
intents.messages= True
intents.message_content = True
allowed_mentions = discord.AllowedMentions(everyone = True)
bot = commands.Bot(command_prefix=';', intents=intents)

# This is something for the ascii bot lel

ascii_chars_light_to_dark = [
  ' ', '.', '_',  ':',  '/',  '=', '$', '#', '@', '░', '▒', '▓', '█'
]

ascii_chars_dark_to_light = ascii_chars_light_to_dark[::-1]

def image_to_ascii(image, ascii_chars, max_width=100):
    image = image.convert('L')
    width, height = image.size

    aspect_ratio = height / width
    new_width = min(max_width, width)
    new_height = int(aspect_ratio * new_width * 0.55) 
    image = image.resize((new_width, new_height))
    pixels = list(image.getdata())
    ascii_str = ''

    for i in range(new_height):
        for j in range(new_width):
            pixel_value = pixels[i * new_width + j]
            ascii_str += ascii_chars[pixel_value * len(ascii_chars) // 256]
        ascii_str += '\n'

    return ascii_str


@bot.event
async def on_ready():
    print(f"Hey! you're running on {bot.user.name}.")
        
# _______ COMMAND CODES __________

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
async def bft(ctx):
            comds = os.popen("sh Brewfetch.sh").read()
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

@bot.command()
async def uptime(ctx):
            """
            
    """

            comd = os.popen("uptime").read()
            comd.replace("`", "\\`")
            
            printer = f"```\n{comd}\n```"
            await ctx.send(printer)

@bot.command()
async def ping(ctx):
 await ctx.send("Pong!")
 
@bot.command()
async def random(ctx):
            """
            20 Random characters from /dev/random
    """

            comd = os.popen("head -c 100 /dev/random | tr -dc 'A-Za-z0-9' | head -c 20").read()
            comd.replace("`", "\\`")
            
            printer = f"\n{comd}\n"
            await ctx.send(printer)

@bot.command()
async def img2ascii(ctx):
    await ctx.send("Initializing :3")
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        try:
            image_bytes = await attachment.read()
            image = Image.open(io.BytesIO(image_bytes))


            if image.format not in ['JPEG', 'PNG']:
                await ctx.send('your image has to be either a PNG or a JPEG')
                return

            ascii_art = image_to_ascii(image, ascii_chars_light_to_dark, max_width=40)

            max_message_length = 2000 - 8 - 6  
            if len(ascii_art) > max_message_length:
                ascii_art = ascii_art[:max_message_length]  
            await ctx.send(f'```\n{ascii_art}\n```')
            await ctx.send("converted °3°")
        except Exception as e:
            await ctx.send(f'an error occurred. Details:\n{str(e)}')
    else:
        await ctx.send("no image attached, showing help / suggestion menu.\nSuggested images aspect ratios are 1:1 and possibly 4:3. because i still lack a proper palette (goddamnit alex aperture science), your images may look like crap, :<  ")

@bot.command()
async def gnuify(ctx, arg):
    await ctx.send(f"GNU/{arg}")
    
bot.run("ADD_TOKEN")
