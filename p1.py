#placer
from pathlib import Path
from PIL import Image, ImageFont, ImageDraw
import os

#フォント読込み
font_file = r'C:\SDtool\000\tool\fonts\SourceHanSans-Normal.otf'
font1 = ImageFont.truetype(font=font_file, size=30, index=0)
font2 = ImageFont.truetype(font=font_file, size=200, index=0)
#文字読込み
with open("JIS.txt", encoding="utf-8") as f:
    text = f.read()

# text = "あいうyutuyrtyrutrwerthyreｒちゅｒｙｔｔるゆｔｒｙｔりゅｒｙつｙちｙちうｙatkuyt"


textList = [text[i:i+16*16] for i in range(0,len(text), 16*16)]
for k in range(len(textList)):
    texts = textList[k]
    ##画像作成
    rowLength = 16
    columnLength = (len(texts)+rowLength-1)//rowLength
    #各文字につき wxh = 200x300
    image_size = (200*rowLength, 300*columnLength)
    im = Image.new(mode='RGB', size=image_size, color=(255, 255, 255))

    ##描画
    draw = ImageDraw.Draw(im)
    for i in range(len(texts)):
        x = (i%16)*200
        y = (i//16)*300

        draw.text(xy=(x,y), text=" "+texts[i]+" uni"+hex(ord(text[i]))[2:], font=font1, fill=(200, 200, 200))
        draw.text(xy=(x,y-20), text=texts[i], font=font2, fill=(250, 250, 250))
        
        draw.rectangle([(x,y+270/1490*300), (x+200, y+1070/1490*300)], outline=(200,200,200), width=1)
        draw.rectangle([(x,y), (x+200, y+300)], outline=(150,150,150), width=4)
    ##画像保存
    bbox = im.getbbox()
    im_crop = im.crop(box=bbox)
    dirname = "dist"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    im_crop.save(dirname+"/"+str(k)+".png")
