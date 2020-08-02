from PIL import Image
image_path = '../images/test.png'
image_path_2 = '../images/test_2.png'
img = Image.open(image_path)
img_2 = Image.open(image_path_2)
img.paste(img_2, box=(300, 200))
img.save('../images/out_paste.png')