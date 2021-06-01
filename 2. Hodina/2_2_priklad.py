import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 720))

running = True

hlava = (100, 100)
telo = (100, 160)
nohy = (100, 260)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.draw.circle(screen, (255, 255, 255), hlava, 20)
    pygame.draw.circle(screen, (255, 255, 255), telo, 40)
    pygame.draw.circle(screen, (255, 255, 255), nohy, 60)

    pygame.display.update()

pygame.quit()