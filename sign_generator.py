from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont 
import os

SELECTED_FONT = "TheSans-B7Bold.otf"
START_RANGE = 1400
END_RANGE = 1520
HEIGHT_IMG = 256
WIDTH_IMG = 256

def main():    
    font = ImageFont.truetype(os.getcwd() + "\\" + SELECTED_FONT, size=90)    
    for i in range(START_RANGE, END_RANGE+1):
        img = Image.new("RGB", (WIDTH_IMG, HEIGHT_IMG), color=(1, 59, 8))
        dr = ImageDraw.Draw(img)
        _, _, w, h = dr.textbbox((0, 0), str(i), font=font)
        dr.text(((WIDTH_IMG-w)/2, (HEIGHT_IMG-h)/2), str(i), font=font, fill=(254, 254, 254))
        img.save("output/" + str(i) + ".jpg")
 
if __name__ == "__main__":
    main()