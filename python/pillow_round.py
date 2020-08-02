from PIL import Image, ImageDraw
prof_size = (500,500)
img_layer = Image.new('L', prof_size)
draw = ImageDraw.Draw(img_layer)
draw.ellipse([(0, 0), img_layer.size], fill=255)
image_path = '../images/test.png'
img = Image.open(image_path)
img_prof = img.copy()
img_prof = img_prof.resize(prof_size)
img_prof.putalpha(img_layer)
#img_prof.save('../images/out_prof.png')
margin = 50
back_size = (prof_size[0] + margin, prof_size[1] + margin)
img_back = Image.new('RGB',back_size , (0, 0, 128))
#img_back.save('../images/out_back.png')
img_back.paste(img_prof,box=(margin//2, margin//2) ,mask=img_prof)
img_back.save('../images/out_round.png')