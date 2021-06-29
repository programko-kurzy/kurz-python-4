import pygame

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()

running = True
background = pygame.image.load('./images/background-day.png').convert_alpha()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    screen.fill((255, 255, 255))

    screen.blit(background, (0,0))

    pygame.display.update()
    clock.tick(60)
pygame.quit()