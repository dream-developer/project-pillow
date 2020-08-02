from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
# 画像の 幅, 高さ 
img_w, img_h = img.size
# 切り抜くサイズ（幅, 高さ）
crop_w, crop_h = (300, 200)
left  = (img_w - crop_w) // 2
upper = (img_h - crop_h) // 2
right = (img_w + crop_w) // 2
lower = (img_h + crop_h) // 2
img_crop = img.crop((left, upper, right, lower))
img_crop.save('../images/out_crop_2.png')