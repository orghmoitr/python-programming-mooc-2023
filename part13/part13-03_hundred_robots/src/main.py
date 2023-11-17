# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0, 0, 0))

x_val = width - 600
x_pos = x_val
y_val = height - 380
for i in range(10):
    for j in range(10):
        window.blit(robot, (x_pos, y_val))
        x_pos += (robot_width-10)
    x_val += 15
    x_pos = x_val
    y_val += 25

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
