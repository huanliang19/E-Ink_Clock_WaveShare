from PIL import Image, ImageDraw, ImageFont

class block:
    # canvas = Image.new('1',(0, 0),255)
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = Image.new('1',(width, height),255)

    # font = ImageFont.load_default()
    # font_size = 1
    # draw = ImageDraw.Draw(canvas)
    # text = ""

    def setFont(self, font):
        self.font = font

    def setFontSize(self, font_size):
        self.font_size = font_size

    def update(self):
        print('helloz')
        return Image.open('100x100.bmp')

class timeBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        print('helloz')
        return Image.open('100x100.bmp')

class dateBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        return Image.open('100x100.bmp')

class dayBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        return Image.open('100x100.bmp')

class factBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        text = "filler text"
        # super().text = wrap_text(text, width=400, font=font)
        # super().text = "\n".join(text)
        return Image.open('100x100.bmp')

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
