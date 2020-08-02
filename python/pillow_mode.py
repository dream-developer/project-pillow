from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
img.convert("1").save('../images/out_convert_1.png')
img.convert("L").save('../images/out_convert_L.png')