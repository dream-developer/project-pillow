from PIL import Image, ImageDraw
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
draw.rectangle([(50, 50), (200, 200)], fill=(0, 0, 255))
img.save('../images/out_rectangle.png')