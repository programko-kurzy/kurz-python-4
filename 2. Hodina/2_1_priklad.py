import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 720))

running = True
dom = pygame.Rect(100, 100, 100, 100)
strecha = [(100, 100), (200, 100), (150, 50)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.draw.rect(screen, (200, 200, 200), dom)
    pygame.draw.polygon(screen, (0, 0, 255), strecha)

    pygame.display.update()

pygame.quit()