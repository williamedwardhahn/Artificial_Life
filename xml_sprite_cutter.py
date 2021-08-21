import os
import xml.etree.ElementTree as ET
import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
from skimage import io as io


def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x, cmap = 'gray')
    ax.axis('off')
    fig.set_size_inches(18, 10)
    plt.show()


# https://www.kenney.nl/assets/simple-space

images_url = "https://github.com/williamedwardhahn/Artificial_Life/raw/main/images/spritesheet_vehicles.png"

xml_url = "https://github.com/williamedwardhahn/Artificial_Life/raw/main/images/spritesheet_vehicles.xml"

os.system("wget " + images_url);

os.system("wget " + xml_url);

names = []

tree = ET.parse("spritesheet_vehicles.xml")
map = {}
for node in tree.iter():
    if node.attrib.get('name'):
        name = node.attrib.get('name')
        names.append(name)
        map[name] = {}
        map[name]['x'] = int(node.attrib.get('x'))
        map[name]['y'] = int(node.attrib.get('y'))
        map[name]['width'] = int(node.attrib.get('width'))
        map[name]['height'] = int(node.attrib.get('height'))





print(names)

r = np.random.randint(0,len(names))

name1 = names[r]
x = map[name1]["x"]
y = map[name1]["y"]
h = map[name1]["width"]
w = map[name1]["height"]

image = io.imread(images_url)[:,:,:3]

plot(image[y:y+w,x:x+h])
