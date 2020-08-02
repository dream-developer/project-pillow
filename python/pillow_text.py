from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('C:\WINDOWS\Fonts\msgothic.ttc', 25)
draw.text((20, 20), "テキスト", font=font, fill=(0,0,255)) 
img.save('../images/out_text.png')