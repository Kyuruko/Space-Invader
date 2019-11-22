import pygame
from title import Title
from game import Game
from game_over import Game_Over
from cores import BLACK
import os


pygame.init()
#configuraçao da tela
size = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('imgs/ufo.png')
bg = pygame.image.load('imgs/game-bg.png')
pygame.display.set_icon(icon)


# cenas devem ser registradas aqui antes de serem usadas
scenes = {
    'title': Title,
    'game': Game,
    'game-over': Game_Over
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

    # permite várias telas (main menu, game, highscore screen, etc)
    if nextscene:
        # permite qualquer tela fecho o jogo
        if nextscene == "exit":
            run = False
            break
        # print(nextscene)
        scene = scenes[nextscene]()
        nextscene = False

    # pressionar tecla, permite várias teclas serem apertadas simultaneamente
    keys = pygame.key.get_pressed()

    # atualiza a img em cada frame
    nextscene = scene.update(keys)

    # limpa tela
    screen.fill(BLACK)

    # desenha tela (cria a img)
    scene.draw(screen)

    # atualiza todos os frames
    pygame.display.update()
