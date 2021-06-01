import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 602))
clock = pygame.time.Clock()

running = True
sky = pygame.image.load('./Sky.png').convert_alpha()
kopce = pygame.image.load('./MountainsBackground.png').convert_alpha()
kopec = pygame.image.load('./Mountain.png').convert_alpha()

sky = pygame.transform.scale(sky, (1024, 602))
kopce = pygame.transform.scale(kopce, (2048, 602))
kopec = pygame.transform.scale(kopec, (1024, 602))

kopec_x = 0

def nakresli_kopce():
    screen.blit(kopec, (kopec_x, 0))
    screen.blit(kopec, (kopec_x - 1024, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    kopec_x += 0.25
    if (kopec_x > 1024):
        kopec_x -= 1024 # aby sa naša pozícia nezväčšovala donekonečna
        # budeme ju po každom prechode vracať o jednu obrazovku späť

    screen.blit(sky, (0, 0))
    nakresli_kopce()

    pygame.display.update()

    clock.tick(60)

pygame.quit()