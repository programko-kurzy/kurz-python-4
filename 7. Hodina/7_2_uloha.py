import pygame

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()


#load images
background = pygame.image.load('./images/background-day.png').convert_alpha()
pipe = pygame.image.load('./images/pipe-green.png').convert_alpha()
pipe2 = pygame.transform.flip(pipe, False, True)
pipe1_rect = pipe.get_rect(center = (150, 512))
pipe2_rect = pipe2.get_rect(center = (150, 0))


# variables
running = True
background_x = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    # update
    background_x -= 1
    if (background_x < -288):
        background_x += 288

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