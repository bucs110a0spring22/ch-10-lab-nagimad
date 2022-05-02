import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("assets/music.mp3")
sound.play()
while pygame.mixer.get_busy():
    pygame.time.delay(100)