from PIL import Image, ImageDraw
fill_back = (0,0,100) # 画像の背景色
fill_bar = (100, 100, 125) # バーの色
width = 220 # 画像の幅
height = 30 # 画像の高さ
img = Image.new('RGB', (width, height) , fill_back)
draw = ImageDraw.Draw(img)
x = 0
y = 10
w = 20
h = height -y*2
y0 = y
y1 = y + h
imgs = []
draw.rectangle([(x + w, y0), ((x + w)*10,y1)], fill=fill_back, outline=fill_bar)
for i in range(1,10):
  x += w
  xy0 = (x, y0)
  xy1 = (x + w, y1)
  draw.rectangle([xy0, xy1], fill=fill_bar)
  img.save('../images/out_bar_'+str(i)+'.png')
for i in range(1,10):
  img = Image.open('../images/out_bar_'+str(i)+'.png')
  imgs.append(img)
imgs[0].save('../images/out_loading.gif', append_images=imgs[1:], save_all=True, loop= 0,duration=500)
