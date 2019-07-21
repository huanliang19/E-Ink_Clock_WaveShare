import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import Block

def wrap_text(text, width, font):
    text_lines = []
    text_line = []
    text = text.replace('\n', ' [br] ')
    words = text.split()
    font_size = font.getsize(text)

    for word in words:
        if word == '[br]':
            text_lines.append(' '.join(text_line))
            text_line = []
            continue
        text_line.append(word)
        w, h = font.getsize(' '.join(text_line))
        if w > width:
            text_line.pop()
            text_lines.append(' '.join(text_line))
            text_line = [word]

    if len(text_line) > 0:
        text_lines.append(' '.join(text_line))

    return text_lines

canvas = Image.new('1',(400,300),255)
# font = ImageFont.truetype('C:\Windows\Fonts\Ariel', 24)
font = ImageFont.load_default()
draw = ImageDraw.Draw(canvas)
draw.text((10, 20), '2.9inch e-Paper', font = font, fill = 0)

texto = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
novo = wrap_text(texto, width=400, font=font)
nova = "\n".join(novo)
print(novo)

draw.text((0, 0), nova, font = font, fill = 0)
canvas.show()
