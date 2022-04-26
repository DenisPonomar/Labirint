# -*- coding: utf-8 -*-
from PIL import Image
import sys, pygame, time
pygame.init()
ty = time.time()
image = Image.open('lab1.png', 'r')
image.thumbnail(size=(1280,720))
width = image.size[0] 
height = image.size[1] 	
pix = image.load()
lab_png = [[None] * height for i in range(width)]
for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        if a+b+c > 381:
            p = False
        else:
            p = True
        lab_png[i][j] = p
print("Размер булевого массива изображенения", sys.getsizeof(lab_png), "байт")
print("Анализ изображения", time.time()-ty, "с") 

size = width, height
screen = pygame.display.set_mode(size)
#pygame.display.set_mode(size, pygame.FULLSCREEN)
shar_tx = 0
shar_ty = 0
shar_x = 20
shar_y = 20
fps = 60
def Shar():
    global shar_x
    global shar_tx
    shar_tx = shar_x
    global shar_y
    global shar_ty
    shar_ty = shar_y
    pygame.draw.circle(screen, [255, 255, 255], [int(shar_x), int(shar_y)], 10, 0)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        shar_x = shar_x - (2*60/fps)
    if keystate[pygame.K_RIGHT]:
        shar_x = shar_x + (2*60/fps)
    if keystate[pygame.K_DOWN]:
        shar_y = shar_y + (2*60/fps)
    if keystate[pygame.K_UP]:
        shar_y = shar_y - (2*60/fps)
granica_vidimosti = 200
def RTX():
    global shar_x
    global shar_tx
    global shar_y
    global shar_ty
    for i in range(0, width, 3):
        if -granica_vidimosti < shar_x - i < granica_vidimosti:
            for j in range(0, height, 3):
                if -granica_vidimosti < shar_y - j < granica_vidimosti:
                    if lab_png[i][j]:
                        rasst = ((i-shar_x)**2 + (j-shar_y)**2)
                        if rasst > granica_vidimosti**2:
                            continue
                        if rasst == 0:
                            r = 255
                        else:
                            r = int((6250000/(rasst**2)) * 255)
                        if rasst < 100:
                            shar_x = shar_tx
                            shar_y = shar_ty
                        if r > 255:
                            r = 255
                        pygame.draw.circle(screen, [r,r,r], [i+1, j+1], 3, 3)
                
score_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    ty = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 0])
    RTX()
    Shar()
    go_score_font = pygame.font.Font(None, 24)
    fps = 1/(time.time()-ty)
    chislo = str(int(fps))+" fps"
    score_surf = go_score_font.render(chislo, 1, [255, 255, 255])
    screen.blit(score_surf, [width-100, 20])
    pygame.display.flip()
pygame.quit()
