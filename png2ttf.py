"""
png画像を二値化してttfフォントを作るプログラム。nymwaさんのtwahiのコードが原型 https://github.com/nymwa/ttf-twahi

"""
import os
import glob
import fontforge
# make new font
font = fontforge.font()
# 名前の設定
fontname = "font1"
font.fontname   = fontname
font.fondname   = fontname
font.fullname   = fontname
font.familyname = fontname
font.encoding   = "UnicodeFull"
font.version    = "1.0"

pngs = glob.glob("./dist/test/*.png")
pngs2names = lambda png : os.path.splitext(png)[0]
names = list(map(pngs2names, pngs))
for index, name in enumerate(names):
    os.system("magick " + name+".png " + name+".bmp") #png -> bmp
    os.system("potrace -s " + name+".bmp") #bmp -> svg
    
    hexCodepoint = os.path.splitext(os.path.basename(name))[0][3:] #uni0041 -> 0041
    glyph = font.createMappedChar(int("0x"+hexCodepoint, 16))       
    glyph.importOutlines(name+".svg") 
    glyph.transform([1.5,0,0,1.5,0,-120])
    glyph.width = 800
    # glyph.transform([1.5,0,0,1.5,0,0],"noWidth")

    # os.system("del " + name+".bmp") #Tatsutori atowo nigosazu
    # os.system("del " + name+".svg")
    print(str(index + 1)+"/"+str(len(names)))

# for glyph in font.glyphs():
#     glyph.transform([1.5,0,0,1.5,0,0],"noWidth")


font.generate(fontname + '.ttf')
font.close()

