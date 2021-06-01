import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()

running = True
player = pygame.image.load('./Player.png').convert_alpha()
sword = pygame.image.load('./Sword.png').convert_alpha()

# moje premenné
player_x = 0
player_y = 0
rychlost = 2
toci_mec = False
uhol_meca = 0
pohyb_hore = False
pohyb_dole = False
pohyb_doprava = False
pohyb_dolava = False

def spracuj_keydown(event):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava, toci_mec
    if event.key == pygame.K_w:
        pohyb_hore = True
    if event.key == pygame.K_s:
        pohyb_dole = True
    if event.key == pygame.K_a:
        pohyb_dolava = True
    if event.key == pygame.K_d:
        pohyb_doprava = True
    if event.key == pygame.K_SPACE:
        toci_mec = True

def spracuj_keyup(event):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava, toci_mec
    if event.key == pygame.K_w:
        pohyb_hore = False
    if event.key == pygame.K_s:
        pohyb_dole = False
    if event.key == pygame.K_a:
        pohyb_dolava = False
    if event.key == pygame.K_d:
        pohyb_doprava = False
    if event.key == pygame.K_SPACE:
        toci_mec = False

def pohyb_hraca():
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava, toci_mec, player_x, player_y, uhol_meca
    if (pohyb_hore):
        if (player_y > 0):
            player_y -= rychlost
    if (pohyb_dole):
        if (player_y < 720):
            player_y += rychlost
    if (pohyb_dolava):
        if (player_x > 0):
            player_x -= rychlost
    if (pohyb_doprava):
        if (player_x < 1024):
            player_x += rychlost
    if (toci_mec):
        uhol_meca -= 5
        if (uhol_meca < -360):
            uhol_meca += 360

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            spracuj_keydown(event)
        if event.type == pygame.KEYUP:
            spracuj_keyup(event)

    pohyb_hraca()
    
    otoceny_mec = pygame.transform.rotate(sword, uhol_meca)
    screen.fill((255, 255, 255))
    screen.blit(player, (player_x, player_y))
    screen.blit(otoceny_mec, (player_x+20, player_y))

    pygame.display.update()
    clock.tick(60)
pygame.quit()