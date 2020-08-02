from PIL import Image
img = Image.new('RGB', (800, 500), (128, 128, 128))
img.save('../images/out_new.png')