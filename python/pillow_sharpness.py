from PIL import Image, ImageEnhance
image_path = '../images/test.png'
img = Image.open(image_path)
enhancer = ImageEnhance.Sharpness(img)
img_res = enhancer.enhance(2.0)
img_res.save('../images/out_sharpness.png')