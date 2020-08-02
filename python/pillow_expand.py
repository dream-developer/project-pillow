from PIL import Image, ImageOps
image_path = '../images/test.png'
img = Image.open(image_path)
img_res = ImageOps.expand(img, border=50, fill=(0,255,255))
img_res.save('../images/out_expand.png')