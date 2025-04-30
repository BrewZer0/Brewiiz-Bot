from PIL import Image

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
    new_height = int(aspect_ratio * new_width * 2)  
    image = image.resize((new_width, new_height))
    pixels = list(image.getdata())
    ascii_str = ''

    for i in range(new_height):
        for j in range(new_width):
            pixel_value = pixels[i * new_width + j]
            ascii_str += ascii_chars[pixel_value * len(ascii_chars) // 256]
        ascii_str += '\n'

    return ascii_str

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

       
            ascii_art = image_to_ascii(image, ascii_chars_light_to_dark, max_width=40)

            
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