from PIL import Image, ImageDraw
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
draw.polygon([(50, 50), (200, 200),(50, 200)])
img.save('../images/out_polygon.png')