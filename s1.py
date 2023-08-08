from PIL import Image
import os
import glob
from datetime import datetime

def ImgSplit(im):
    # 読み込んだ画像を200*300のサイズで54枚に分割する
    width = 200
    height = 300

    # 縦の分割枚数
    for i in range(16):
        # 横の分割枚数
        for j in range(16):
            w2 = j * width
            h2 = i * height
            yield im.crop((w2, h2, w2 + width, h2 + height))

# if __name__ == '__main__':

#文字読込み
with open("JIS.txt", encoding="utf-8") as f:
    text = f.read()

#画像一覧の取得
dirname = "./dist/"
tables = glob.glob(dirname + "*.png")
for index, table in enumerate(tables):
    # 画像の読み込み
    im = Image.open(dirname + str(index) + ".png")
    print(table)
    for i, img in enumerate(list(ImgSplit(im))):
        # 保存先フォルダの指定

        if not os.path.exists(dirname+"test/"):
            os.mkdir(dirname+"test/")
        code_point = "uni"+hex(ord(text[i+index*256]))[2:]
        img.save(dirname+"test/"+code_point+".png","png")
