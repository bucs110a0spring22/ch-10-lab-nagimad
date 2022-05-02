import pygame
from pygame.locals import *
from pygame import mixer

 
mixer.init()
mixer.music.load('assets/01 Title.mp3')
mixer.music.play()
 
runing = True
while runing:
    window.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()
