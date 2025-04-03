from PIL import Image, ImageDraw, ImageFont
import random as rnd
from datetime import datetime

print('enter your email:')
email = input()

def extract_chars(email):
    email.replace("@","")
    split = email.split('.')

    firstLetter = split[0][0]
    lastLetter = split[1][0] if len(split) > 1 else ''

    return firstLetter.upper(), lastLetter.upper()


def draw_avatar(email):

    firstLetter, lastLetter = extract_chars(email)

    chars = firstLetter + lastLetter
    colortheme = (rnd.randint(0,255), rnd.randint(0,255), rnd.randint(0,255))
    imagesize = (128,128)
    fontsize = 50

    img = Image.new('RGB', imagesize, colortheme)
    draw = ImageDraw.Draw(img)


    try:
        fnt = ImageFont.truetype("Roboto-Light.ttf", fontsize)
    except IOError:
        fnt = ImageFont.load_default() #If font isn't available goes back to default
    
    text_w = draw.textlength(chars, font=fnt)
    text_h = fontsize

    text_x = (imagesize[0] - text_w) // 2
    text_y = (imagesize[1] - text_h) // 2

    draw.text((text_x, text_y), chars, fill=(255,255,255), font=fnt)

    # timestamp for filename
    now = datetime.now()
    timestamp = int(datetime.timestamp(now))

    img.save(f"{timestamp}.png")

draw_avatar(email)