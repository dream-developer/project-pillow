from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
# 画像の 幅, 高さ 
img_w, img_h = img.size
left = img_w // 4
upper = img_h // 4
right = (img_w // 4) * 3
lower = (img_h // 4) * 3
img_crop = img.crop((left, upper, right, lower))
img_crop.save('../images/out_crop.png')