import numpy as np
import matplotlib.pyplot as plt
import pygame
from pygame import surfarray

N = 256

pygame.init()
display = pygame.display.set_mode((N,N))


def montage_plot(x):
    x = np.pad(x, pad_width=((0, 0), (1, 1), (1, 1)), mode='constant', constant_values=0)
    return montage(x)

def draw_ball(x,y):
    y*=-1
    N = 256
    r = 2
    U = np.zeros((N,N)) 
    U[y+N//2-r:y+N//2+r,x+N//2-r:x+N//2+r] = 1
    return U

def draw_left_paddle(y):
    x = -100
    y*=-1
    N = 256
    r = 2
    l = 8
    U = np.zeros((N,N)) 
    U[y+N//2-(r+l):y+N//2+(r+l),x+N//2-r:x+N//2+r] = 1
    return U

def draw_right_paddle(y):
    x = 100
    y*=-1
    N = 256
    r = 2
    l = 8
    U = np.zeros((N,N)) 
    U[y+N//2-(r+l):y+N//2+(r+l),x+N//2-r:x+N//2+r] = 1
    return U

def render(x,y,p1,p2):

    U = draw_ball(x,y) + draw_left_paddle(p1) + draw_right_paddle(p2)

    return U

def rn():
    return (1 * np.sign(np.random.randn(b,))).astype(int)

def ry():
    return np.random.randint(-3,3,size=(b,))

def rp():
    return np.random.randint(-n,n,size=(b,))

###############################################################

"""## Parallel Main Loop"""

b = 10

N = 256
n = N//2 - 10

x = np.zeros(b,).astype(int)
y = np.zeros(b,).astype(int)

dx = rn().astype(int)
dy = rn().astype(int) 

p1 = rp().astype(int) # ypos
p2 = rp().astype(int)

dp2 = 0

s1 = np.zeros(b,).astype(int) #score
s2 = np.zeros(b,).astype(int) 

steps = 1000

MAX_BOUNCE_ANGLE = (2/3)*np.pi

print("Start game...")

for i in range(steps):

    x  -= dx
    y  -= dy
    

    c0 = np.abs(y) > n              #hit top or bottom wall
    c1 = (x < -92)                  #past left wall 
    c2 = (x >  92)                  #past right wall
    c3 = c1 * (np.abs(p1 - y) < 8)  #hit left paddle
    c4 = c2 * (np.abs(p2 - y) < 8)  #hit right paddle
    c5 = c3 + c4                    #hit left or hit right 
    c6 = (x < -110)             #past left wall but miss paddle
    c7 = (x >  110)             #past right wall but miss paddle


    dy[c0] *= -1 #flip dy if hit top or botton wall


    dx[c5] *= -1 #flip dx and dy if paddle hit
    dy[c5] *= -1

    
    s2[c6] +=1 #score player2 and reset
    x[c6] = 0
    y[c6] = 0
    dx[c6] = rn().astype(int)[c6]
    dy[c6] = rn().astype(int)[c6] 


    s2[c7] +=1 #score player1 and reset
    x[c7] = 0
    y[c7] = 0
    dx[c7] = rn().astype(int)[c7]
    dy[c7] = rn().astype(int)[c7] 

    p1 = p1 - (p1 - y)
#    p2 = p2 - (p2 - y)
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up was pressed")
                dp2 = 3

            if event.key == pygame.K_DOWN:
                print("down was pressed")
                dp2 = -3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("up was released")
                dp2 = 0

            if event.key == pygame.K_DOWN:
                print("down was released")
                dp2 = 0
    p2 += dp2
    

    img = 255*(render(x[0],y[0],p1[0],p2[0]).T)
    img = np.stack((img,img,img),2)
    surfarray.blit_array(display, img)
    pygame.display.update()

    plt.pause(0.008)

pygame.quit()











#    if len(y[c5]) > 0:
#        dx[c5] = ((np.sqrt(dx[c5]**2+dy[c5]**2))*np.cos((p1 - y[c5])*MAX_BOUNCE_ANGLE/4))
#        dy[c5] = ((np.sqrt(dx[c5]**2+dy[c5]**2))*np.cos((p1 - y[c5])*MAX_BOUNCE_ANGLE/4))
#        dx[c5] = ((np.sqrt(dx[c5]**2+dy[c5]**2))*np.cos((p2 - y[c5])*MAX_BOUNCE_ANGLE/4))
#        dy[c5] = ((np.sqrt(dx[c5]**2+dy[c5]**2))*np.cos((p2 - y[c5])*MAX_BOUNCE_ANGLE/4))


