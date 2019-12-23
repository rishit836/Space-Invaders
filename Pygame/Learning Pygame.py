import pygame
import random as r

pygame.init()

game_win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

random_place = r.randint(0, (800 - 64))
ufo = pygame.image.load('ufo.png')
playerIMG = pygame.image.load('space-invaders.png')
playerx = 370
playery = 480
clock = pygame.time.Clock()
fps = 64
change_x = 0
endportal = 750
enemyIMG = pygame.image.load('space-ship.png')
enemyx = random_place
enemyy = 50
change = True
bullet = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_state = "ready"
bullet_speed = 15
enemy_Y_change_1 = 1
enemy_X_change_1 = 0.5
score = 0

background = pygame.image.load('background.png')

enemyx_change = 0

pygame.display.set_icon(ufo)


def player():
    game_win.blit(playerIMG, (playerx, playery))


def enemy():
    game_win.blit(enemyIMG, (enemyx, enemyy))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    game_win.blit(bullet, (x + 16, y + 10))


Running = True

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_x = 12
            elif event.key == pygame.K_LEFT:
                change_x = -12
            elif event.key == pygame.K_SPACE:
                bullet_x = playerx
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                change_x = 0
            if event.key == pygame.K_LEFT:
                change_x = 0

    if playerx == 0:
        playerx += 10

    if playerx == endportal:
        playerx -= 10

    playerx += change_x
    game_win.fill((0, 0, 0))
    game_win.blit(background, (0, 0))

    if bullet_y <= 0:
        bullet_state = "ready"
        bullet_y = 480
        bullet_speed = 0

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed
        bullet_speed = 15

    # collision detection
    if (bullet_x - enemyx) < 10 and (bullet_y - enemyy) < 0:
        print("Collision True")
        score += 1
        print("Score is " + str(score))
        random_place = r.randint(0, (800 - 64))
        enemyx = random_place
        enemyy = 50
        bullet_state = "ready"
        bullet_x = playerx + 16
        bullet_y = 480 + 10

    if enemyx == (800 - 64):
        enemy_X_change_1 = enemy_X_change_1 * -1

    if enemyx == 0:
        enemy_X_change_1 = enemy_X_change_1 * -1

    player()
    enemy()
    clock.tick(fps)

    # enemy change physics

    enemyy += enemy_Y_change_1
    enemyx += enemy_X_change_1
    pygame.display.update()

quit()
