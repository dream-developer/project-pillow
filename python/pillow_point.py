from PIL import Image, ImageDraw
img = Image.new('RGB', (100, 100), (128, 128, 128))
draw = ImageDraw.Draw(img)
draw.point((50,50), fill=(0,0,255))
img.save('../images/out_point.png')