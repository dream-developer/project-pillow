from PIL import Image, ImageDraw, ImageFont
image_path = '../images/test.png'
img = Image.open(image_path)
img_design_size = (img.width, img.height//3)
img_design = Image.new('RGBA', img_design_size , (0, 0, 0, 128))
draw = ImageDraw.Draw(img_design)
font = ImageFont.truetype('C:\WINDOWS\Fonts\msgothic.ttc', 50)
draw.text((150, 30),"つくえのうえの\nコーヒーカップ", font=font, fill=(255,255,255), align="center") 
img.paste(img_design, box=(0, img.height//3), mask=img_design)
img.save('../images/out_eyecatch_2.png')
