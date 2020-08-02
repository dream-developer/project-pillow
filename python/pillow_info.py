from PIL import Image
image_path = "../images/test.png"
img = Image.open(image_path)
# ファイル名(パス):../images/test.png
print(f'ファイル名(パス):{img.filename}')
# フォーマット:PNG
print(f'フォーマット:{img.format}')
# サイズ:(652, 532)
print(f'サイズ:{img.size}')
# 幅, 高さ:(652, 532)
print(f'幅, 高さ:{(img.width, img.height)}')
