import pygame

class Game_Over:
    def __init__(self):
        self.bg = pygame.image.load('imgs/game-over.png').convert_alpha()

    # funcao que reseta a tela de GO, para o menu principal
    def update(self, keys,keypress):
        if keys[pygame.K_r]:
            return "title"

    # desenha a tela de GO
    def draw(self,screen):
        screen.blit(self.bg, (0, 0))