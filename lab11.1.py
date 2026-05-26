import os
from PIL import Image, ImageFilter

fdir = r"C:\Users\Анастасия\Pictures"
di = r"C:\Users\Анастасия\Downloads\images-py"

os.makedirs(di, exist_ok=True)

for i in os.listdir(fdir):
    way = os.path.join(fdir, i)
    if os.path.isfile(way):
        try:
            img = Image.open(way)
            fmg = img.filter(ImageFilter.EDGE_ENHANCE)
            name, form = os.path.splitext(i)
            way2 = os.path.join(di, f"{name}-filtred{form}")
            fmg.save(way2)
            print(f"изменен файл: {i}")
        except Exception as k:
            print(f"Не удалось изменить {i}: {k}")