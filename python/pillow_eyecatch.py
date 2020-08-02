from PIL import Image, ImageDraw, ImageFont
image_path = '../images/test.png'
img = Image.open(image_path)
img_design_size = img.size
img_design = Image.new('RGBA', img_design_size , (255, 255, 255, 128))
draw = ImageDraw.Draw(img_design)
font = ImageFont.truetype('C:\WINDOWS\Fonts\msgothic.ttc', 50)
draw.text((150, 30),"つくえのうえの\nコーヒーカップ", font=font, fill=(0,0,0), align="center") 
img.paste(img_design, mask=img_design)
img.save('../images/out_eyecatch.png')
