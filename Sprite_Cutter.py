# William Edward Hahn
# August 2021
import pygame
import button
import csv
import pickle
import numpy as np
from skimage.io import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 640
lower_margin = 100
side_margin = 300

screen = pygame.display.set_mode((screen_width + side_margin, screen_height + lower_margin))
pygame.display.set_caption('sprite cutter')


font = pygame.font.SysFont('futura', 30)

def draw_text(text, font, text_color, x, y):
	img = font.render(text, True, text_color)
	screen.blit(img, (x, y))


sprite_sheet0    = pygame.image.load('img/farmglobal.png').convert_alpha()
sprite_sheet_img = imread('img/farmglobal.png')[:,:,:3]


def draw_bg():
	screen.fill((0,0,0))
	
	sprite_sheet = pygame.transform.scale(sprite_sheet0, (int(z*sprite_sheet0.get_width()), int(z*sprite_sheet0.get_height())))
	
	screen.blit(sprite_sheet, (0,0))


	

x = 0
y = 0
h = 16
w = 16

z = 1

counter = 0 

run = True
while run:

	clock.tick(fps)

	draw_bg()

	pygame.draw.rect(screen, (255,0,0), (int(z*(x-1)),int(z*(y-1)),int(z*(w+1)),int(z*(h+1))), 1)



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_UP:
				y -= 1
			if event.key == pygame.K_DOWN: 
				y += 1
			if event.key == pygame.K_LEFT: 
				x -= 1
			if event.key == pygame.K_RIGHT: 
				x += 1
				

			if event.key == pygame.K_KP7:
				h -= 1
			if event.key == pygame.K_KP9:
				h += 1
			if event.key == pygame.K_KP1:
				w -= 1
			if event.key == pygame.K_KP3:
				w += 1



			if event.key == pygame.K_KP2:
				y += h+1
			if event.key == pygame.K_KP8:
				y -= h+1
			if event.key == pygame.K_KP6:
				x += w+1
			if event.key == pygame.K_KP4:
				x -= w+1	
				
				
				
			if event.key == pygame.K_2:
				z += 0.1
			if event.key == pygame.K_1:
				z -= 0.1		
				
				
			print(z,x,y,h,w)	

			if event.key == pygame.K_KP5:
				
				img = sprite_sheet_img[y:y+h,x:x+w] 
		
				imsave("./sprites/sprite_" + str(counter) + ".png",img)	
		
				counter += 1

	pygame.display.update()

pygame.quit()
