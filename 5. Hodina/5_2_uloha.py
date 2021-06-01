import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()

running = True
player = pygame.image.load('./Player.png').convert_alpha()
sword = pygame.image.load('./Sword.png').convert_alpha()
medal = pygame.image.load('./Medal.png').convert_alpha()

# moje premenné
player_rect = player.get_rect(center = (0, 0))

# položíme medailu na náhodné miesto, vrámci našej obrazovky
medal_rect = medal.get_rect(center = (randint(0, 1024), randint(0, 720)))

rychlost = 5
pohyb_hore = False
pohyb_dole = False
pohyb_doprava = False
pohyb_dolava = False

def check_collision():
    global player_rect, medal_rect
    if player_rect.colliderect(medal_rect):
        print("Získal si medailu!")

def spracuj_key(event, hodnota):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava
    if event.key == pygame.K_w:
        pohyb_hore = hodnota
    if event.key == pygame.K_s:
        pohyb_dole = hodnota
    if event.key == pygame.K_a:
        pohyb_dolava = hodnota
    if event.key == pygame.K_d:
        pohyb_doprava = hodnota

def pohyb_hraca():
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava, player_rect
    if pohyb_hore:
        if player_rect.centery > 0:
            player_rect = player_rect.move(0, -rychlost)
    if pohyb_dole:
        if player_rect.centery < 720:
            player_rect = player_rect.move(0, rychlost)
    if pohyb_dolava:
        if player_rect.centerx > 0:
            player_rect = player_rect.move(-rychlost, 0)
    if pohyb_doprava:
        if player_rect.centerx < 1024:
            player_rect = player_rect.move(rychlost, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            spracuj_key(event, True)
        if event.type == pygame.KEYUP:
            spracuj_key(event, False)

    pohyb_hraca()
    check_collision()
    
    screen.fill((255, 255, 255))
    screen.blit(player, player_rect)
    screen.blit(medal, medal_rect)
    screen.blit(sword, player_rect.move(20, 0))

    pygame.display.update()
    clock.tick(60)
pygame.quit()