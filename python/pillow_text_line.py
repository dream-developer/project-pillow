from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (250, 250), (128, 128, 128))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('C:\WINDOWS\Fonts\msgothic.ttc', 25)
draw.text((20, 20),"あいうえお\nかき\nくけこ", font=font, fill=(0,0,255), spacing = 40,  align="center") 
img.save('../images/out_text_line.png')