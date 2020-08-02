from PIL import Image, ImageEnhance
image_path = '../images/test.png'
img = Image.open(image_path)
enhancer = ImageEnhance.Brightness(img)
img_res = enhancer.enhance(0.5)
img_res.save('../images/out_brightness.png')