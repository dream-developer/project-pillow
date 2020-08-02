from PIL import Image, ImageDraw
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
draw.line([(20,20), (125,230)], fill=(0,0,255), width=10)
img.save('../images/out_line.png')