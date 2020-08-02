from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
img_putalpha = img.copy()
img_putalpha.putalpha(128)
img_putalpha.save('../images/out_putalpha.png')