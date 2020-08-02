from PIL import Image, ImageDraw
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
draw.ellipse([(50, 50), (200, 200)])
img.save('../images/out_ellipse.png')