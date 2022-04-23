# -*- coding: utf-8 -*-
import sys, pygame, random, os, time
pygame.init()
pygame.mixer.init()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
shar_x = 500
shar_y = 325
def Shar():
    global shar_x
    global shar_y
    pygame.draw.circle(screen, [255, 255, 255], [int(shar_x), int(shar_y)], 10, 0)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
        shar_x = shar_x - 1
    if keystate[pygame.K_RIGHT]:
        shar_x = shar_x + 1
    if keystate[pygame.K_DOWN]:
        shar_y = shar_y + 1
    if keystate[pygame.K_UP]:
        shar_y = shar_y - 1

k = 50
def RTX_gor():
    m1 = [[5, 50], [320, 50]]
    m2 = [[735, 50], [1075, 50]]
    m3 = [[100, 110], [225, 110]]
    m4 = [[640, 110], [865, 110]]
    m5 = [[1075, 110], [1170, 110]]
    m6 = [[545, 170], [965, 170]]
    m7 = [[1075, 170], [1280, 170]]
    m8 = [[100, 240], [640, 240]]
    m9 = [[965, 240], [1175, 240]]
    m10 = [[100, 305], [225, 305]]
    m11 = [[320, 305], [545, 305]]
    m12 = [[840, 305], [1280, 305]]
    m13 = [[0, 365], [545, 365]]
    m14 = [[740, 365], [1170, 365]]
    m15 = [[100, 430], [320, 430]]
    m16 = [[740, 430], [965, 430]]
    m17 = [[0, 490], [220, 490]]
    m18 = [[640, 490], [860, 490]]
    m19 = [[100, 555], [740, 555]]
    m20 = [[840, 555], [965, 555]]
    m21 = [[1075, 555], [1280, 555]]
    m22 = [[420, 620], [545, 620]]
    m23 = [[965, 620], [1180, 620]]
    m24 = [[100, 685], [225, 685]]
    m25 = [[420, 685], [545, 685]]
    m26 = [[925, 685], [1280, 685]]
    mas = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, m24, m25, m26]
    for p in range(26):
        m = mas[p]
        for i in range(m[1][0]-m[0][0]):
            try:
                r = int((k/(((i+m[0][0]-shar_x)**2 + (m[0][1]-shar_y)**2)**0.5))**2 *255)
            except ZeroDivisionError:
                r = 255
            if r > 255:
                r = 255
            pygame.draw.circle(screen, [r,r,r], [i+m[0][0], m[0][1]], 1, 1)


def RTX_ver():
    m1 = [[0, 40], [0, 720]]
    m2 = [[100, 110], [100, 240]]
    m3 = [[100, 555], [100, 620]]
    m4 = [[225, 165], [225, 305]]
    m5 = [[225, 555], [225, 685]]
    m6 = [[320, 50], [320, 185]]
    m7 = [[320, 305], [320, 365]]
    m8 = [[320, 430], [320, 555]]
    m9 = [[320, 605], [320, 720]]
    m10 = [[420, 0], [420, 240]]
    m11 = [[420, 430], [420, 620]]
    m12 = [[545, 50], [545, 170]]
    m13 = [[545, 365], [545, 495]]
    m14 = [[545, 620], [545, 685]]
    m15 = [[640, 0], [640, 110]]
    m16 = [[640, 240], [640, 555]]
    m17 = [[640, 620], [640, 720]]
    m18 = [[740, 170], [740, 365]]
    m19 = [[740, 555], [740, 685]]
    m20 = [[965, 50], [740, 240]]
    m21 = [[965, 365], [740, 620]]
    m22 = [[1075, 50], [1075, 110]]
    m23 = [[1075, 430], [1075, 555]]
    m24 = [[1170, 40], [1170, 110]]
    m25 = [[1170, 365], [1170, 490]]
    m26 = [[1280, 720], [1280, 685]]
    mas = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, m24, m25, m26]
    for p in range(26):
        m = mas[p]
        for i in range(m[1][1]-m[0][1]):
            try:
                r = int((k/(((m[0][0]-shar_x)**2 + (i+m[0][1]-shar_y)**2)**0.5))**4 *255)
            except ZeroDivisionError:
                r = 255
            if r > 255:
                r = 255
            pygame.draw.circle(screen, [r,r,r], [m[0][0], i+m[0][1]], 1, 1)
score_font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    ty = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 0])
    
    
    RTX_gor()
    RTX_ver()
    Shar()
    pygame.display.flip()
    clock.tick(50)
    #print int(1/(time.time()-ty))
pygame.quit()
if "restart" in locals():
    if restart == True:
        os.system("zombiv1.0.py")
