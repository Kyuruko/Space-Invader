import pygame
from cores import YELLOW

class HUD:
    score = 0
    def __init__(self):
        HUD.score=0
        self.vida_player = 2
        self.font = pygame.font.Font("fonts/times.ttf", 24)
        self.text = self.font.render("Score: ", True, YELLOW)

    # escreve na tela o texto
    def draw(self, screen):
        screen.blit(self.text, (25, 570))

    # escreve o texto do score
    def update(self, keys):
        self.text = self.font.render("Score: "+str(HUD.score), True, YELLOW)

    # atualiza o valor do score
    def add_score(self, score = 100):
        HUD.score += score


