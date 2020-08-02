from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
img_transpose = img.transpose(Image.TRANSVERSE)
img_transpose.save('../images/out_transpose.png')