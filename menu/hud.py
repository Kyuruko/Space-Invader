import pygame
from cores import YELLOW

class HUD:
    def __init__(self):
        self.score = 0
        self.vida_player = 2
        self.font = pygame.font.Font("fonts/times.ttf", 24)
        self.text = self.font.render("Score: ", True, YELLOW)

    # escreve na tela o texto
    def draw(self, screen):
        screen.blit(self.text, (25, 570))

    # escreve o texto do score
    def update(self, keys):
        self.text = self.font.render("Score: "+str(self.score), True, YELLOW)

    # atualiza o valor do score
    def add_score(self, score = 100):
        self.score += score


