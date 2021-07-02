import pygame
import numpy as np
from pygame import surfarray

pygame.init()

w = 256
h = 256

display = pygame.display.set_mode((w, h))

while True:

    img = 256*np.random.random((256,256,3))


    surfarray.blit_array(display, img)
    pygame.display.flip()


pygame.quit()
