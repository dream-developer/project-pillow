from PIL import Image, ImageFilter
image_path = '../images/test.png'
img = Image.open(image_path)
img = img.filter(ImageFilter.BLUR)
img.save('../images/out_blur.png')