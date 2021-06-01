import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 720))

running = True

points = [(200, 100), (175, 200), (250, 150), (150, 150), (250, 200)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.draw.polygon(screen, (255, 255, 0), points)

    pygame.display.update()

pygame.quit()