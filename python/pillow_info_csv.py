from PIL import Image
import csv
from glob import glob
image_path_list = glob('../images/*.png')
with open('image_info.csv', mode='w', encoding='utf-8', newline='') as fp:
  writer = csv.writer(fp)
  # ヘッダー
  writer.writerow(['filename', 'format', 'width', 'height', 'mode'])
  for image_path in image_path_list:
    img = Image.open(image_path)
    writer.writerow([img.filename, img.format, img.width, img.height, img.mode])
