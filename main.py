
# Libraries

import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

# Command List and Variables

help_command_list = {"-h", "--help", "-help", "help", "-?", "--?"}
work_command_list = {"-w", "--work", "-work", "work", "-run", "--run", "run", "-r", "--r"}
mode = ''

uzunluk = 0
genislik = 0

get_file_name = None
get_scale = 0
get_size = 100
get_mode = 'gray'

gray_metin = "@#W$9876543210?!abcdef;:+=-,.   "
color_metin = "@#W$9876543210?!abcdef;:+=-,."

# Some Functions

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
    
# Main

# Detect help mode     

for help in help_command_list:
    if len(sys.argv) == 2:
        if sys.argv[1] == help:
            mode = 'help'
            print_info()
            break 

# If mode is not help

if mode != 'help':
    if len(sys.argv) > 1:

        # Detect work mode  

        for work in work_command_list:
            if sys.argv[1] == work:
                mode = 'work'

                # Get arguments

                for arguments in sys.argv:

                    # If argument is work mode or file name, continue

                    if arguments == sys.argv[0] or arguments == sys.argv[1]:
                        continue
                    else:
                        # Else, parse argument
                        argument = parse_argument(arguments)
                        # Get parsed argument
                        if argument[0] == 'image':
                            get_file_name = str(argument[1])
                        elif argument[0] == 'scale':
                            get_scale = float(argument[1])
                        elif argument[0] == 'size':
                            get_size = int(argument[1])
                        elif argument[0] == 'mode':
                            get_mode = str(argument[1])
                        else:
                            # Get parsed argument is None, so argument is unknown
                            print("ERROR : Unknown argument!")
                            print("For help, type 'py main.py -h' or 'py main.py --help'")
                            break

                # Get Image according to mode
                if get_mode == 'gray':
                    image = cv2.imread(get_file_name, 0)
                elif get_mode == 'color' or get_mode == 'opacity':
                    image = cv2.imread(get_file_name)
                else:
                    # Get Image according to mode is unknown
                    print("ERROR : Unknown mode!")
                    print("For help, type 'py main.py -h' or 'py main.py --help'")
                    break

                # If image file founded
                if image is not None:
                    # Scale image if scale is not 0
                    if get_scale != 0:
                        image = cv2.resize(image, None, fx=get_scale, fy=get_scale)
                    else:
                        # Change image size if scale is 0 (default value is 100)
                        uzunluk = image.shape[0]
                        genislik = image.shape[1]
                        oran = uzunluk / genislik
                        image = cv2.resize(image, (get_size, int(get_size * oran)))

                    # Get image size
                    uzunluk = image.shape[0]
                    genislik = image.shape[1]
                    
                    # Open html file
                    file = open("index.html", "w")

                    if get_mode == 'gray':
                        # Write html file
                        file.write("<html><head><meta charset='utf-8'><title>ASCII Art</title>")
                        file.write('<style>body{margin:0;padding:0;background-color:#000;}</style></head><body>')
                        file.write('<p style="color:#fff;font-family: monospace;font-size: 10px;line-height: 10px;white-space: pre;letter-spacing: 5px;">')
                        file.write('\n')
                        # Write html file with characters
                        for i in range(uzunluk):
                            for j in range(genislik):
                                # Detect character according to pixel value
                                dizi_indis = map(image[i][j], 0, 255, 0, len(gray_metin) - 1)
                                file.write(gray_metin[int(dizi_indis)])
                            file.write('\n')
                        file.write('</p></body></html>')
                    elif get_mode == 'color':
                        # Detect image's gray scale
                        imageBlack = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                        # Write html file
                        file.write('<html><head><meta charset="utf-8"><title>ASCII Art</title><link rel="stylesheet" href="style.css">')
                        file.write('</head><body>')
                        # Create row div
                        file.write('<div class="row">')
                        file.write('\n')
                        # Write html file with characters
                        for i in range(uzunluk):
                            # Create column div(s)
                            file.write('<div class="col">')
                            file.write('\n')
                            for j in range(genislik):
                                # Create pixel div(s) and get pixel color
                                file.write('<div class="pixel" style="color:rgb(' + str(image[i][j][2]) + ',' + str(image[i][j][1]) + ',' + str(image[i][j][0]) + ')">')
                                # Detect character according to pixel value
                                dizi_indis = map(imageBlack[i][j], 0, 255, 0, len(color_metin) - 1)
                                file.write(color_metin[int(dizi_indis)])
                                file.write('</div>')
                            file.write('\n')
                            file.write('</div>')
                        file.write('</div></body></html>')
                    # Close html file
                    file.close()
                else:
                    # File not founded
                    print("ERROR : File not found!")
                    print("For help, type 'py main.py -h' or 'py main.py --help'")
                    break

        # If mode is not work

        if mode != 'work':
            print("ERROR : Unknown command!")
            print("For help, type 'py main.py -h' or 'py main.py --help'")
    # If no arguments
    else:
        print("ERROR : No arguments!")
        print("For help, type 'py main.py -h' or 'py main.py --help'")
        