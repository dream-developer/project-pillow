from PIL import Image, ImageFilter
image_path = '../images/test.png'
img = Image.open(image_path)
img = img.filter(ImageFilter.EDGE_ENHANCE)
img.save('../images/out_edge_enhance.png')