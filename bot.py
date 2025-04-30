import discord
from discord.ext import commands
import io
import os
import logging
from PIL import Image

from scripts import ascii

print("Brewiiz Bot Runner\n (C) 2025 Brewy. Some Rights Reserved.")

logging.basicConfig(level=logging.INFO)
intents = discord.Intents.default()
intents.messages= True
intents.message_content = True
allowed_mentions = discord.AllowedMentions(everyone = True)
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.command()
async def ascii_gen(ctx):
    await ctx.send("Initializing :3")
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        try:
            image_bytes = await attachment.read()
            image = Image.open(io.BytesIO(image_bytes))

            if image.format not in ['JPEG', 'PNG']:
                await ctx.send('Unsupported image format. Please upload a JPEG or PNG image.')
                return

         
            await ctx.send("we're doing ts... one secondish :]")

       
            ascii_art = ascii.image_to_ascii(image, ascii.ascii_chars_light_to_dark, max_width=40)

            
            max_embed_length = 4096 - 10 
            if len(ascii_art) > max_embed_length:
                ascii_art = ascii_art[:max_embed_length]  
            embed = discord.Embed(title="Result", description=f'```\n{ascii_art}\n```')
            
            await ctx.send(embed=embed)
            await ctx.send("generated °3°")
        except Exception as e:
            await ctx.send(f'# Oops. \nan error occurred. Details:\n{str(e)}')
    else:
        await ctx.send(" attach an image. i can't generate anything mate :(")

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
async def todo(ctx):
	await ctx.send('to do:\n- add linux commands:\n- try suggestions for it')

@bot.command()
async def calc(ctx, *, expression: str):
    """
    calculate some mathematical expressions.
    """
    try:
        expression = expression.replace(',', '.')
        result = eval(expression, {"__builtins__": None}, {})
        await ctx.send(f"; expression: {expression}\n; result: {result}")
    
    except Exception as e:
        await ctx.send(f"Error in calculation: {e}")

@bot.command()
async def command(ctx, cmd):
    """
    Runs a command. Commands MUST be enclosed in \"s.
    """

    # todo: add more characters that might freak discord's markdown parser out
    phobia = ['`']

    cmd = os.popen(cmd).read()
    for phobes in phobia:
        cmd.replace(phobes, f"\{phobes}")

    await ctx.send(cmd)

  
@bot.command()
async def presents(ctx):
         await ctx.send("**Hi, i'm Brewiiz, a bot coded in discord.py.**\n i was originally a thousand different things, starting from robot liberabot (viznut, you're the fucking goat of demos) back in i guess january 2025. i forgor 💀\n\nSlightly based from **Buck's BrewBot code** which solved my whole issue with embedding GNU/Linux commands to linux for shits and giggles (as simple as an os.popen statement, almost).\n i will expand to add more functionalities from other bots, such as an image to ASCII converter. Hope you use me as i upgrade and... contribute if you can code with discord.py.\nComing soon to a github near you :3\n-# Brewiiz PFP by <@1300105674285387898>. ")         


@bot.command()
async def gnuify(ctx, arg):
    await ctx.send(f"GNU/{arg}")
    
bot.run("ADD_TOKEN")