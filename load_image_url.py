import numpy as np
from skimage import io as io
import matplotlib.pyplot as plt
from skimage.util import view_as_blocks

def plot(x):
    fig, ax = plt.subplots()
    im = ax.imshow(x, cmap = 'gray')
    ax.axis('off')
    fig.set_size_inches(18, 10)
    plt.show()

image = io.imread("https://opengameart.org/sites/default/files/chicken_walk.png")

# image = image[:32,:32,:3]/255.0

images = view_as_blocks(image, block_shape=(32,32,4))

print(images.shape)

plot(images[3,0,0,:,:,:])
