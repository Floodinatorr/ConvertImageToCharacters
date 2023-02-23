import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = 'araba.jpg'
size = 150
metin = "@#W$9876543210?!abcdef;:+=-,.   "

img = cv2.imread(file_name, 0)

a, b = img.shape
oran = a / b
imageBlack = cv2.resize(img, (size, int(size * oran)))
uzunluk, genislik = imageBlack.shape

def map(x, in_min, in_max, out_min, out_max):
    islem1 = (x - in_min) * (out_max - out_min)
    islem2 = in_max - in_min
    return (islem1 / islem2) + out_min

with open('index.html', 'w') as file:
    file.write('<style>body{margin:0;padding:0;background-color:#000;}</style>')
    file.write('<p style="color:#fff;font-family: monospace;font-size: 10px;line-height: 10px;white-space: pre;letter-spacing: 5px;">')
    file.write('\n')
    for i in range(uzunluk):
        for j in range(genislik):
            dizi_indis = map(imageBlack[i][j], 0, 255, 0, len(metin) - 1)
            file.write(metin[int(dizi_indis)])
        file.write('\n')
    file.write('</p>')
