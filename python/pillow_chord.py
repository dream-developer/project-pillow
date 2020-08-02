from PIL import Image, ImageDraw
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
draw.chord([(50, 50), (200, 200)], start=120, end=260, fill=(0, 0, 255), outline=(255, 255, 0), width=3)
img.save('../images/out_chord.png')