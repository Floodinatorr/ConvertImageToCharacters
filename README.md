# Convert Images To Characters

Hi guys!

### How It Works?

The system developed with Python and OpenCV. System gets image and converts it to characters. The system has 2 different modes. The first mode is "Normal" mode. In this mode, the system converts the image to characters. The second mode is "Color" mode. In this mode, the system converts the image to characters and colors.

> Note: The system has a problem with the color mode. The system can't convert the image to characters and colors perfectly. I will fix this problem in the future releases. 

### How To Use?

First, you need to install the requirements. You can install requirements with the command below.

```bash
pip install -r requirements.txt
```

Then, you need to run the system. You can run the system with the command below. 

```bash
python main.py -w image=image_name.jpg
```

> Note 1: You can use any image format, name or path.
> Note 2: You must write the image name. If you don't write the image name, the system will rasie an error.

You can change scale of image with the command below.

```bash
python main.py -w image=image_name.jpg scale=0.5
```

You can change size(px) with the command below.

```bash
python main.py -w image=image_name.jpg size=100
```

> Note: You can use only one of scale or size. If you use both of them, the system will use the "scale" parameter.

Finally, you can see the result with opening the "index.html" file.

### Preview

Normal:

<img style="display:block;" src="https://raw.githubusercontent.com/Floodinatorr/ConvertImageToCharacters/main/normal.jpg" data-canonical-src="https://raw.githubusercontent.com/Floodinatorr/ConvertImageToCharacters/main/normal.jpg" width="480" height="300" />

Converted:

<img style="display:block;" src="https://raw.githubusercontent.com/Floodinatorr/ConvertImageToCharacters/main/final.png" data-canonical-src="https://raw.githubusercontent.com/Floodinatorr/ConvertImageToCharacters/main/final.png" width="480" height="300" />

