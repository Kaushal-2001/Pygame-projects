import pygame
import math
import random

#always initialise the game
pygame.init()

# game screen
screen = pygame.display.set_mode((800, 629))

pygame.display.set_caption("Cupid balloon")

background =pygame.image.load("balloonback.png")


# creating a player
playerImg = pygame.image.load("gun.png")
playerX = 10
playerY = 75
playerY_change = 0

#creating an object to shoot
balloonImg = []
balloonX = []
balloonY = []
balloonY_change = []
num_of_balloons = 4

for i in range(num_of_balloons ):
    balloonImg.append(pygame.image.load('balloon.png'))
    balloonX.append(random.randint(570, 736))
    balloonY.append(random.randint(0, 50))
    balloonY_change.append(0.1)


bulletImg = pygame.image.load("bullet.png")
bulletX = 10
bulletY = 0
bulletX_change = 1
bulletY_change = 3
bullet_state = "ready"







# Main game loop
running = True

while running:

    screen.fill((0,0,0))

    screen.blit(background, (0,0))

    def player(x,y):
        screen.blit(playerImg , (x , y))

    def balloon(x, y, i):
        screen.blit(balloonImg[i] , (x , y))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 20, y + 4))


    def isCollision(balloonX, balloonY, bulletX, bulletY):
        distance = math.sqrt((math.pow(balloonX - bulletX, 2)) + math.pow(balloonY - bulletY, 2))
        if distance < 27:
            return True
        else:
            return False




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change = 3
            if event.key == pygame.K_UP:
                playerY_change = -3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletY = playerY
                    fire_bullet(bulletX,bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0


    if playerY <= 0:
        playerY = 0
    elif playerY >=534:
        playerY = 534
    playerY += playerY_change



    for i in range(num_of_balloons):
        if balloonY[i] >= 565  :
            running = False
            print("Game Over")

        balloonY[i] += balloonY_change[i]

        collision = isCollision(balloonX[i], balloonY[i], bulletX, bulletY)
        if collision:
            bulletX = 0
            bullet_state = "ready"
            balloonX[i] = random.randint(550,736)
            balloonY[i] = random.randint(0, 50)



        balloonY[i] += balloonY_change[i]
        balloon(balloonX[i], balloonY[i], i)

    if bulletX >= 750:
        bulletX = 0
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletX += bulletX_change

    player(playerX, playerY)

    pygame.display.update()


