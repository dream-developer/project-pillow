from PIL import Image, ImageOps
image_path = '../images/test.png'
img = Image.open(image_path)
img_res = ImageOps.autocontrast(img, cutoff=50)
img_res.save('../images/out_autocontrast.png')