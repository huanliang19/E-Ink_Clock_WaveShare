from PIL import Image, ImageDraw, ImageFont

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

class block:
    def __init__(self, xy, width, height):
        x, y = xy
        self.width = 0
        self.height = 0

    def printText(self, text):
        pass

class timeBlock(block):
    def setTime(hour, minutes, ampm):
        pass

class dateBlock(block):
    def setDate(month, day, year):
        pass

class dayBlock(block):
    def setDay(day):
        pass

class factBlock(block):
    def updateFact():
        pass
