from PIL import Image, ImageFilter
image_path = '../images/test.png'
img = Image.open(image_path)
img = img.filter(ImageFilter.FIND_EDGES)
img.save('../images/out_find_edges.png')