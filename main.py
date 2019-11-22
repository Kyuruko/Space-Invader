import pygame
import os
#colors

RED = (150, 0, 0)
LRED = (255, 0, 0)
GREEN = (0, 150, 0)
LGREEN = (0, 255, 0)
BLUE = (0, 0, 150)
LBLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (150, 0, 150)
LPURPLE = (255, 0, 255)
COLORS = [RED, LRED, GREEN, LGREEN, BLUE, LBLUE, WHITE, PURPLE, LPURPLE]
#display config
size = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('imgs/ufo.png')
background = pygame.image.load('imgs/game-bg.png')
pygame.display.set_icon(icon)


# scenes must be registered here before being used
scenes = {
    'title': Title,
    'game': Game
}
nextscene = "title"

run = True
# game loop
while run:
    for event in pygame.event.get():
        # close the app if needed
        if event.type == pygame.QUIT:
            run = False
            break

    # allows for multiple screens (main menu, game, highscore screen, etc)
    if nextscene:
        # allow for any screen to quit the game
        if nextscene == "exit":
            run = False
            break
        # print(nextscene)
        scene = scenes[nextscene]()
        nextscene = False

    # keys pressed, allows for multiple keys to be pressed at the same time.
    keys = pygame.key.get_pressed()

    # updates screen and their objects positions and other magical stuff
    nextscene = scene.update(keys)

    # clear the screen
    screen.fill(BLACK)

    # draws screen
    scene.draw(screen)

    # update everything
    pygame.display.update()
