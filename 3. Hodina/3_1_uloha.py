import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 602))
clock = pygame.time.Clock()

running = True
sky = pygame.image.load('./Sky.png').convert_alpha()
kopce = pygame.image.load('./MountainsBackground.png').convert_alpha()
kopec = pygame.image.load('./Mountain.png').convert_alpha()
stromy_pozadie = pygame.image.load('./MountainTrees.png').convert_alpha()
stromy = pygame.image.load('./Forest.png').convert_alpha()

sky = pygame.transform.scale(sky, (1024, 602))
kopce = pygame.transform.scale(kopce, (2048, 602))
kopec = pygame.transform.scale(kopec, (1024, 602))
stromy_pozadie = pygame.transform.scale(stromy_pozadie, (2048, 602))
stromy = pygame.transform.scale(stromy, (2048, 602))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    screen.blit(sky, (0, 0))
    screen.blit(kopce, (0, 0))
    screen.blit(stromy_pozadie, (0, 0))
    screen.blit(kopec, (0, 0))
    screen.blit(stromy, (0, 0))
    pygame.display.update()

    clock.tick(60)

pygame.quit()