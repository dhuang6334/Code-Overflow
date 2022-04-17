import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
color = (0, 0, 0)
screen.fill(color)
pygame.display.flip()
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(30)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False

    screen.blit(pygame.image.load('images/left/LA1.png'), (0,0))
    pygame.display.update()