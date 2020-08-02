from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
img_thumbnail = img.copy()
img_thumbnail.thumbnail((326, 326))
img_thumbnail.save('../images/out_thumbnail.png')
