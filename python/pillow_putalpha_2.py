from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
img_2 = img.copy()
# アルファ付き(透過画像)にする
img_2.putalpha(128)
# サイズを縮小
img_2 = img_2.resize((img.width//2, img.height//2))
# mask で指定する
img.paste(img_2, mask=img_2)
img.save('../images/out_putalpha_2.png')