import pygame


class Enemy:
    def __init__(self, X=0, Y=0):
        self.e_X = X
        self.e_Y = Y

        self.velocidade = 0.2
        self.direcao = 1

    def update(self):
        self.X = self.X + self.direcao * self.velocidade
        if self.X > 736 or self.X < 0:
            self.direcao =  self.direcao * -1
            self.Y = self.Y + 64 + 4
