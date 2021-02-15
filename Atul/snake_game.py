import pygame
import random

pygame.init()
dis = pygame.display.set_mode((600, 400))
pygame.display.update()

pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
blue = (0,0,255)
red = (255, 0, 0)
black = (0, 0, 0)

# initial position of the snake
x = 300
y = 300

clock = pygame.time.Clock()

game_running = True

while game_running:
    pygame.display.update()
    (x_food, y_food) = (random.randrange(590), random.randrange(390))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        # Arrow key Press Event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10

    dis.fill(black)
    pygame.draw.rect(dis, blue, [x, y, 10, 10])
    pygame.draw.rect(dis, white, [x_food, y_food, 10, 10])
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()