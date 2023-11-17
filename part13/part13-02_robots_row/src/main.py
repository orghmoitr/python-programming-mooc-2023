# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
x_value = robot.get_width()
y_value = robot.get_height()

window.fill((0, 0, 0))
x_position = 50
y_position = height-380
for i in range(10):
    window.blit(robot, (x_position, y_position))
    x_position += x_value
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
