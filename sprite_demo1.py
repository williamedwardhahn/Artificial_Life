import pygame
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

image = io.imread("https://opengameart.org/sites/default/files/chicken_walk.png")[:,:,:3]


# image = io.imread("https://opengameart.org/sites/default/files/sheep_walk.png")[:,:,:3]

# plot(image)

up    = 0 
left  = 1
down  = 2
right = 3


images = view_as_blocks(image, block_shape=(32,32,3))

avatar = images[3,0,0,:,:,:]

avatar = np.fliplr(avatar)
avatar = np.rot90(avatar,k=1,axes=(0,1))
avatar = pygame.surfarray.make_surface(avatar)

avatars = [[pygame.surfarray.make_surface(np.rot90(np.fliplr(images[j,i,0,:,:,:]),k=1,axes=(0,1))) for i in range(4)] for j in range(4)]

pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MPCR Demo 1')

# avatar = pygame.image.load('img/avatar.png').convert()
# avatar = np.random.randn(100,100,3)
# avatar = pygame.surfarray.make_surface(avatar)

clock = pygame.time.Clock()
fps = 5


run = True
while run:
    

    for i in range(100):
        
        screen.fill((0,0,0))

        screen.blit(avatars[up][i%4], ( 400, 400 - i*10 ))
        
        screen.blit(avatars[down][i%4], ( 400, 400 + i*10 ))
        
        screen.blit(avatars[left][i%4], ( 400 - i*10, 400 ))
        
        screen.blit(avatars[right][i%4], ( 400 + i*10, 400 ))
        
        



        clock.tick(fps)
        pygame.display.update()
    

    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		run = False

pygame.quit()
