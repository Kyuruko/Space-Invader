import pygame
from menu.title import Title
from game.game import Game
from menu.game_over import Game_Over
from menu.showscore import ShowScore
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
    'game-over': Game_Over,
    'show-score': ShowScore
}
nextscene = "title"

run = True
keypress = None
# game loop
while run:
    for event in pygame.event.get():
        # fecha a janela
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.KEYDOWN:
            keypress = event
        elif event.type == pygame.KEYUP:
            keypress = None
    pygame.event.clear()

    # permite várias telas (main menu, game, highscore screen, etc)
    if nextscene:
        # tela de quit do jogo
        if nextscene == "exit":
            run = False
            break
        # print(nextscene)
        scene = scenes[nextscene]()
        nextscene = False

    # pressionar tecla, permite várias teclas serem apertadas simultaneamente
    keys = pygame.key.get_pressed()

    # atualiza a img em cada frame
    nextscene = scene.update(keys,keypress)

    # limpa tela
    screen.fill(BLACK)

    # desenha tela (cria a img)
    scene.draw(screen)

    # atualiza todos os frames
    pygame.display.update()
