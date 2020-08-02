from PIL import Image, ImageOps
image_path = '../images/test.png'
img = Image.open(image_path)
img_gray = ImageOps.grayscale(img)
img_res = ImageOps.colorize(img_gray, black=(0, 0, 35), white=(220, 220, 255))
img_res.save('../images/out_colorize.png')