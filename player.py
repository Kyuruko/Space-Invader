import pygame
import os


class Player:
    def __init__(self, X = 370, Y = 480):
        self.p_X = X
        self.p_Y = Y

        self.velocidade = 0.4

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.X += -self.velocidade
        if keys[pygame.K_RIGHT]:
            self.X += self.velocidade

        if self.X <= 0:
            self.X = 0
        elif self.X >= 736:
            self.X = 736
