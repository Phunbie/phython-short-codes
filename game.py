import pygame

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('background.png')
planet = pygame.image.load('p_one.png')
planet_x = 140
move_direction = 'right'
spaceship = pygame.image.load('spaceship.png')
bullet = pygame.image.load('bullet.png')
bullet_y = 500
fired = False

# Step 1: create clock variable here
clock = pygame.time.Clock()

keep_alive = True
while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True:
        fired = True

    if move_direction == 'right':
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = 'right'


    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            fired = False
            bullet_y = 500
    screen.blit(background, [0, 0])
    screen.blit(planet, [planet_x, 50])
    screen.blit(bullet, [180, bullet_y]) 
    screen.blit(spaceship, [160, 500])
    pygame.display.update()
    # step 2: add clock tick here
    clock.tick(60)