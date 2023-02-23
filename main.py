import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

help_command_list = {"-h", "--help", "-help", "help", "-?", "--?"}
work_command_list = {"-w", "--work", "-work", "work", "-run", "--run", "run", "-r", "--r"}
mode = ''

uzunluk = 0
genislik = 0

get_file_name = None
get_scale = 0
get_size = 100
get_mode = 'gray'

metin = "@#W$9876543210?!abcdef;:+=-,.   "

def map(x, in_min, in_max, out_min, out_max):
    islem1 = (x - in_min) * (out_max - out_min)
    islem2 = in_max - in_min
    return (islem1 / islem2) + out_min

def print_info():
    print("Usage: py main.py -w [file_name] [scale_or_size] [mode]")
    print("Example: py main.py -w image=araba.jpg scale=0.5 mode=normal_black_white")
    print("Mode List:")
    print("- Gray Scale [gray]: This mode is more simple than others. App will convert image to gray scale and print it with characters.")
    print("- Color Scale [color]: This mode is same with Gray Scale mode, but this mode has colors. App will convert image to gray scale and print it with characters. All characters has got a color from image.")
    print("- Opacity Scale [opacity]: This mode is same with Color Scale mode, but this mode has opacity. App will convert image to gray scale and print it with characters. All characters has got a color from image and a opacity from image. Opacity value gets from image's gray scale pixel value.")

def parse_argument(argument):
    a = argument.split("=")
    if a[0] == 'image' or a[0] == 'scale' or a[0] == 'size' or a[0] == 'mode':
        return a
    else:
        return None    

for help in help_command_list:
    if len(sys.argv) == 2:
        if sys.argv[1] == help:
            mode = 'help'
            print_info()
            break 
    
if mode != 'help':
    if len(sys.argv) > 1:
        for work in work_command_list:
            if sys.argv[1] == work:
                mode = 'work'
                for arguments in sys.argv:
                    if arguments == sys.argv[0] or arguments == sys.argv[1]:
                        continue
                    else:
                        argument = parse_argument(arguments)
                        if argument[0] == 'image':
                            get_file_name = str(argument[1])
                        elif argument[0] == 'scale':
                            get_scale = float(argument[1])
                        elif argument[0] == 'size':
                            get_size = int(argument[1])
                        elif argument[0] == 'mode':
                            get_mode = str(argument[1])
                        else:
                            print("Unknown argument!")
                            print_info()
                            break

                if get_mode == 'gray':
                    image = cv2.imread(get_file_name, 0)
                elif get_mode == 'color' or get_mode == 'opacity':
                    image = cv2.imread(get_file_name)
                else:
                    print("Unknown mode!")
                    print_info()
                    break
                
                if image is not None:
                    if get_scale != 0:
                        image = cv2.resize(image, None, fx=get_scale, fy=get_scale)
                    else:
                        uzunluk = image.shape[0]
                        genislik = image.shape[1]
                        oran = uzunluk / genislik
                        image = cv2.resize(image, (get_size, int(get_size * oran)))

                    uzunluk = image.shape[0]
                    genislik = image.shape[1]
                    
                    file = open("index.html", "w")
                    file.write("<html><head><meta charset='utf-8'><title>ASCII Art</title>")
                    file.write('<style>body{margin:0;padding:0;background-color:#000;}</style></head><body>')
                    file.write('<p style="color:#fff;font-family: monospace;font-size: 10px;line-height: 10px;white-space: pre;letter-spacing: 5px;">')
                    file.write('\n')
                    print(uzunluk,genislik)
                    for i in range(uzunluk):
                        for j in range(genislik):
                            dizi_indis = map(image[i][j], 0, 255, 0, len(metin) - 1)
                            file.write(metin[int(dizi_indis)])
                        file.write('\n')
                    file.write('</p></body></html>')
                    file.close()
                else:
                    print("File not found!")
                    break

        if mode != 'work':
            print_info()
    else:
        print_info()
        