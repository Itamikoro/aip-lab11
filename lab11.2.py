import os
from PIL import Image


fdir = r"C:\Users\Анастасия\Pictures"
form = ('.jpg', '.png')

for name in os.listdir(fdir):
    if name.lower().endswith(form):
        way = os.path.join(fdir, name)
        try:
            img = Image.open(way)
            print("файл:", name)
            print("Размер: ", img.size, "ширина, высота")
            print("Формат: ", img.format)
            print("Цветовая модель: ", img.mode)
        except FileNotFoundError:
            print("Файл не найден")