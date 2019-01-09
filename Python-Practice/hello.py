import pygame

pygame.init()

background_color =  (255, 255, 255)
(height, width) = (800, 600)

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Trial 1")
screen.fill(background_color)

pygame.display.flip()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed == True
            quit()