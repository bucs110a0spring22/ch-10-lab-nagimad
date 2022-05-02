import pygame

'''add the music file from the assets 
arg:mixer'''

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("assets/music.ogg")
sound.play()
while pygame.mixer.get_busy():
    pygame.time.delay(100)
