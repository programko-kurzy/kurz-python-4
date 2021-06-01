import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()

running = True
player = pygame.image.load('./Player.png').convert_alpha()

# moje premenné
player_x = 0
player_y = 0
rychlost = 2
pohyb_hore = False
pohyb_dole = False
pohyb_doprava = False
pohyb_dolava = False

def spracuj_keydown(event):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava
    if event.key == pygame.K_w:
        pohyb_hore = True
    if event.key == pygame.K_s:
        pohyb_dole = True
    if event.key == pygame.K_a:
        pohyb_dolava = True
    if event.key == pygame.K_d:
        pohyb_doprava = True

def spracuj_keyup(event):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava
    if event.key == pygame.K_w:
        pohyb_hore = False
    if event.key == pygame.K_s:
        pohyb_dole = False
    if event.key == pygame.K_a:
        pohyb_dolava = False
    if event.key == pygame.K_d:
        pohyb_doprava = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            spracuj_keydown(event)
        if event.type == pygame.KEYUP:
            spracuj_keyup(event)

    if (pohyb_hore):
        player_y -= rychlost
    if (pohyb_dole):
        player_y += rychlost
    if (pohyb_dolava):
        player_x -= rychlost
    if (pohyb_doprava):
        player_x += rychlost
    
    screen.fill((255, 255, 255))
    screen.blit(player, (player_x, player_y))

    pygame.display.update()
    clock.tick(60)
pygame.quit()