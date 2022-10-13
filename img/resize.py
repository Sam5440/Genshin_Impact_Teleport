from PIL import Image
import os

print("Resize images in the folder")
folder = input("folder: ")
##w = int(input("width: "))
##h = int(input("height: "))
for i in os.listdir(folder):
    file = f"{folder}\\{i}"
    im = Image.open(file)
    im = im.resize((30, 30), Image.ANTIALIAS)
    im.save(file)