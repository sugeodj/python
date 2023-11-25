from PIL import Image, ImageEnhance, ImageFilter
import os

path = r'G:\My Drive\Code\ImageEditor\imgs'
pathOut = r'G:\My Drive\Code\ImageEditor\out'

for file in os.listdir(path):
    img = Image.open(f'{path}/{file}')
    edit = img.filter(ImageFilter.SHARPEN)
    name = os.path.splitext(file)[0]
    edit.save(f'{pathOut}/{name}_edited.png')
    print(f'{file} edited successfully!')
