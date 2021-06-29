import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()


#load images
background = pygame.image.load('./images/background-day.png').convert_alpha()
pipe = pygame.image.load('./images/pipe-green.png').convert_alpha()
pipe2 = pygame.transform.flip(pipe, False, True)


# variables
running = True
background_x = 0
pipe1_rect = pipe.get_rect(center = (218, 512))
pipe2_rect = pipe2.get_rect(center = (218, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    # update
    background_x -= 1
    if (background_x < -288):
        background_x += 288

    pipe1_rect = pipe1_rect.move(-2, 0)
    pipe2_rect = pipe2_rect.move(-2, 0)

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

    pygame.display.update()
    clock.tick(60)
pygame.quit()