from PIL import Image
# pngファイルを開く
image_path = '../images/test.png'
img = Image.open(image_path)
# jpg形式で保存、画質は80とする。
img.save('../images/out_jpg.jpg', quality=80)
