from menu.hud import HUD
import pygame


class High_Score:
    def __init__(self):
        self.hd_bg = pygame.image.load("imgs/high-score-bg.png")
        self.placar_open = open("menu/high-score.txt", "r")
        self.arq = self.placar_open.readlines()
        self.get_score = int(self.arq[0])
        self.score = self.hud.score
        self.hud = HUD()
    def updateArq(self):
        if self.get_score < int(self.score):
            self.placar_open.close()
            self.arq = open("high-score.txt", "w")
            self.arq.write(str(self.score))
            self.arq.close()

            return self.score
        return self.get_score

    def draw(self, screen):
        screen.blit(self.hd_bg, (0,0))
