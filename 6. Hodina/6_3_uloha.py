import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()

running = True
walk_frames = []
idle_frames = []
coin_idle = []
for i in range(1, 7):
    walk_frames.append(pygame.image.load('./walk/walk0'+str(i)+'.png').convert_alpha())
for i in range(1, 5):
    idle_frames.append(pygame.image.load('./idle/idle0'+str(i)+'.png').convert_alpha())
for i in range(6):
    coin_idle.append(pygame.image.load('./coin_idle/tile00'+str(i)+'.png').convert_alpha())


# moje premenné
current_frame = 0
player_rect = idle_frames[current_frame].get_rect(center = (0, 0))

# položíme medaile na náhodné miesta, vrámci našej obrazovky
coins = []
for i in range(5):
    coins.append(coin_idle[0].get_rect(center = (randint(0, 1024), randint(0, 720))))

ANIMATION_EVENT = pygame.USEREVENT
pygame.time.set_timer(ANIMATION_EVENT, 200)

rychlost = 2
pohyb_hore = False
pohyb_dole = False
pohyb_doprava = False
pohyb_dolava = False

moje_mince = 0

def check_collision():
    global player_rect, coins, moje_mince
    for i in range(len(coins)):
        if player_rect.colliderect(coins[i]):
            moje_mince += 1
            coins[i].update(randint(0, 1024), randint(0, 720), coins[i].width, coins[i].height)
            print("Získal si mincu!")
            print("Doteraz si nazbieral:", moje_mince, "mincí")

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

def kracanie():
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava
    return pohyb_dolava or pohyb_dole or pohyb_hore or pohyb_doprava

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            spracuj_key(event, True)
        if event.type == pygame.KEYUP:
            spracuj_key(event, False)
        if event.type == ANIMATION_EVENT:
            current_frame += 1

    check_collision()
    pohyb_hraca()
    
    screen.fill((255, 255, 255))
    if ( kracanie() ):
        to_draw = walk_frames[current_frame % 6]
    else: 
        to_draw = idle_frames[current_frame % 4]
    if pohyb_dolava:
        to_draw = pygame.transform.flip(to_draw, True, False)
    
    for i in range(len(coins)):
        screen.blit(coin_idle[current_frame % 6], coins[i])

    screen.blit(to_draw, player_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()