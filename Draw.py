import Block

canvas = Image.new('1',(400,300),255)
# font = ImageFont.truetype('C:\Windows\Fonts\Ariel', 24)
font = ImageFont.load_default()
draw = ImageDraw.Draw(canvas)
draw.text((10, 0), 'hello3333333jjjjjjjjjjj', font = font, fill = 0)
draw.text((10, 20), '2.9inch e-Paper', font = font, fill = 0)

texto = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
novo = textwrap.wrap(texto, width=20)
draw.text((10, 0), nova, font = font, fill = 0)

canvas.show()
