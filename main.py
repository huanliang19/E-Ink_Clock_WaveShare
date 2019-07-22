#!/usr/bin/python
# -*- coding:utf-8 -*-

# import epd4in2
import Block as blk
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

timeLoc = (0,0)
dateLoc = (200,0)
dayLoc = (200,40)
factLoc = (0,80)

try:
#     epd = epd4in2.EPD()
#     epd.init()
#     epd.Clear(0xFF)

    # Drawing on the Horizontal image
    # Himage = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)  # 255: clear the frame
    Himage = Image.new('1', (400, 300), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    # font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 24)

    timeBlk = blk.timeBlock(200,80)
    dateBlk = blk.dateBlock(200,40)
    dayBlk = blk.dayBlock(200,40)
    factBlk = blk.factBlock(400,220)

    timeImg = timeBlk.update()
    dayImg = dateBlk.update()
    dateImg = dayBlk.update()
    factImg = factBlk.update()

    bmp = Image.open('100x100.bmp')
    Himage.paste(timeImg, timeLoc)
    Himage.paste(bmp, dateLoc)
    Himage.paste(bmp, dayLoc)
    Himage.paste(bmp, factLoc)

    # epd.display(epd.getbuffer(Himage))
    Himage.show()
    time.sleep(2)


    # print("read bmp file")
    # Himage = Image.open('4in2.bmp')
    # epd.display(epd.getbuffer(Himage))
    # time.sleep(2)
    #
    # print("read bmp file on window")
    # Himage2 = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)  # 255: clear the frame
    # bmp = Image.open('100x100.bmp')
    # Himage2.paste(bmp, (50,10))
    # epd.display(epd.getbuffer(Himage2))
    # time.sleep(2)

    # epd.sleep()

except:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()
