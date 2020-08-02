from PIL import Image
image_path = '../images/test_2.png'
img = Image.open(image_path)
imgs = [img.rotate(i) for i in range(45,361,45)]
imgs[0].save('../images/out_gif.gif', append_images=imgs[1:], save_all=True, duration=1000)