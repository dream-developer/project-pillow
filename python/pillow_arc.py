from PIL import Image, ImageDraw
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
draw.arc([(50, 50), (200, 200)], start=120, end=260)
img.save('../images/out_arc.png')