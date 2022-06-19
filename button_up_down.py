import pygame

x = 0
 
N = 256
pygame.init()
display = pygame.display.set_mode((N,N))


def dx():
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				return -1
			if event.key == pygame.K_RIGHT:
				return 1
	return 0


while True:
    print(x)
    
    x += dx()
