from PIL import Image, ImageOps
image_path = '../images/test.png'
img = Image.open(image_path)
img_res = ImageOps.invert(img)
img_res.save('../images/out_invert.png')