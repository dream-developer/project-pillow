from PIL import Image, ImageDraw, ImageFont
image_path = '../images/test.png'
img = Image.open(image_path)
img_design_size = (img.width//3, img.height//3)
img_design = Image.new('RGBA', img_design_size , (120, 80, 40, 128))
draw = ImageDraw.Draw(img_design)
font = ImageFont.truetype('C:\WINDOWS\Fonts\msgothic.ttc', 25)
draw.text((15, 40),"つくえのうえの\nコーヒーカップ", spacing=20, font=font, fill=(255, 255, 255), align="center") 
img.paste(img_design, box=(img.width//2, img.height//2), mask=img_design)
img.save('../images/out_eyecatch_3.png')
