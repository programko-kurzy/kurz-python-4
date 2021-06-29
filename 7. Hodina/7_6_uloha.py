import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()


#load images
background = pygame.image.load('./images/background-day.png').convert_alpha()
pipe = pygame.image.load('./images/pipe-green.png').convert_alpha()
bird1 = pygame.image.load('./images/bluebird-downflap.png').convert_alpha()
bird2 = pygame.image.load('./images/bluebird-midflap.png').convert_alpha()
bird3 = pygame.image.load('./images/bluebird-upflap.png').convert_alpha()
bird_frames = [bird1, bird2, bird3]

pipe2 = pygame.transform.flip(pipe, False, True)


# variables
running = True
background_x = 0
pipe1_rect = pipe.get_rect(center = (218, 512))
pipe2_rect = pipe2.get_rect(center = (218, 0))

bird_rect = bird1.get_rect(center = (50, 256))
bird_frame = 0

pohyb_hore = 0
max_rychlost = 3
gravitacne_zrychlenie = 0.3

mavanie_kridel = pygame.USEREVENT
pygame.time.set_timer(mavanie_kridel, 200)

# functions
def check_collision():
    global pipe1_rect, pipe2_rect, bird_rect, running
    if bird_rect.colliderect(pipe1_rect) or bird_rect.colliderect(pipe2_rect):
        running = False
        print("Ouch!")

def spracuj_key(event):
    global pohyb_hore
    if event.key == pygame.K_SPACE:
        pohyb_hore = -5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYUP:
            spracuj_key(event)
        if event.type == mavanie_kridel:
            bird_frame += 1
            if (bird_frame > 2):
                bird_frame = 0
    # update
    background_x -= 1
    if (background_x < -288):
        background_x += 288

    pipe1_rect = pipe1_rect.move(-2, 0)
    pipe2_rect = pipe2_rect.move(-2, 0)

    pohyb_hore += gravitacne_zrychlenie
    if (pohyb_hore > max_rychlost):
        pohyb_hore = max_rychlost

    bird_rect = bird_rect.move(0, pohyb_hore)
    if (bird_rect.centery > 550):
        print("Ouch!")
        running = False
        break
        
    check_collision()

    if (pipe1_rect.centerx < -50):
        # posun = randint(-50, 50) BONUS 7.3
        pipe1_rect.centerx = 300
        # pipe1_rect.centery += posun

        pipe2_rect.centerx = 300
        # pipe2_rect.centery += posun

    # draw
    screen.fill((255, 255, 255))

    screen.blit(background, (background_x,0))
    screen.blit(background, (background_x + 288,0))
    #pipes
    screen.blit(pipe, pipe1_rect)
    screen.blit(pipe2, pipe2_rect)
    screen.blit(bird_frames[bird_frame], bird_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()