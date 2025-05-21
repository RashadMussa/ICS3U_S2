import pygame
from pygame.locals import *

"""
A program which just outputs mouse and keyboard events.
"q" quits the program.

Cursor must be inside the game window, and the game
window must have the focus to be responsive.
"""

# Define your keyboard constants for arrow keys and space bar
UpArrow = 1073741906
DownArrow = 1073741905
LeftArrow = 1073741904
RightArrow = 1073741903
SpaceBar = 32

gameOn = True

pygame.init()  # initialize the game window
# pygame needs a window
screen = pygame.display.set_mode((500, 400), 0, 32)  # define the window size and position
pygame.display.set_caption('Drawing - Press q to quit')
WHITE = (255, 255, 255)
screen.fill(WHITE)
count = 0
# sensitivity for mouse moves
# 1 = max sensitivity; larger numbers are less sensitive
sensitivity = 10

while gameOn:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print(event.key)  # still print the key code
            if event.key == K_q:
                gameOn = False
            elif event.key == UpArrow:
                print("Up")
            elif event.key == DownArrow:
                print("Down")
            elif event.key == LeftArrow:
                print("Left")
            elif event.key == RightArrow:
                print("Right")
            elif event.key == SpaceBar:
                print("Space")
        elif event.type == MOUSEMOTION:
            count += 1
            if (count % sensitivity == 0):
                count = 0
                print("you moved the mouse")
        elif event.type == MOUSEBUTTONUP:
            print("mouse button up")
        elif event.type == MOUSEBUTTONDOWN:
            print("mouse button down")
    screen.fill(WHITE)
