import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 602))
clock = pygame.time.Clock()

running = True
sky = pygame.image.load('./Sky.png').convert()
sky = pygame.transform.scale(sky, (1024, 602))
sky_x = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    sky_x += 1
    screen.blit(sky, (sky_x, 0))
    pygame.display.update()

    clock.tick(60)

pygame.quit()