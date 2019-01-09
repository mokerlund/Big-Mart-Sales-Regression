import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Trial 1")

pygame.display.flip()
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed == True
            quit()
        print(event)
    pygame.display.update()
    clock.tick(60)
    print(event)