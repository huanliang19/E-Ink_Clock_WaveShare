from PIL import Image, ImageDraw, ImageFont
import datetime

x = datetime.datetime.now()
class block:
    canvas = Image.new('1',(0, 0),255)
    font = ImageFont.load_default()
    font_size = 1
    draw = ImageDraw.Draw(canvas)
    text = ""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = Image.new('1',(width, height),255)
        self.draw = ImageDraw.Draw(self.canvas)
        self.font_size = 5
        self.font = ImageFont.load_default()

    def setFont(self, font):
        self.font = font

    def generate(self):
        w,h = self.font.getsize(self.text)
        self.draw.text((((self.width)-w)/2, (self.height-h)/2), self.text, font = self.font, fill = 0)
        return self.canvas

class timeBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        self.text = x.strftime("%I") + ":" + x.strftime("%M") + x.strftime("%p")

class dateBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        self.text = x.strftime("%m") + "/" + x.strftime("%d") + "/" + x.strftime("%y")

class dayBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def update(self):
        self.text = x.strftime("%A")

class factBlock(block):
    def __init__(self, width, height):
        super().__init__(width, height)

    def wrap_text(self, text, width, font):
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

    def update(self):
        text = "What is a Pale Ale?\nPale ale is a beer made by warm fermentation using predominantly pale malt. The higher proportion of pale malts results in a lighter colour. The term 'pale ale' first appeared around 1703 for beers made from malts dried with coke, which resulted in a lighter colour than other beers popular at that time."
        tmp = self.wrap_text(text, width=400, font=self.font)
        self.text = "\n".join(tmp)

    def generate(self):
        self.draw.text((0, 0), self.text, font = self.font, fill = 0)
        return self.canvas
