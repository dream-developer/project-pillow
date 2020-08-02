from PIL import Image
image_path = '../images/test.png'
img = Image.open(image_path)
extensions = ['bmp','dib','eps','im','jpg','tga','tiff']
for extension in extensions:
  img.save('../images/out.' + extension)