from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
img_rotate = img.rotate(45, fillcolor=(100,255,255))
img_rotate.save('../images/out_rotate.png')