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