import pygame
import random

class Enemy:
    def __init__(self, X=0, Y=0):
        self.e_X = X
        self.e_Y = Y

        self.velocidade = 0.8
        self.direcao = 1

        self.e_IMG = pygame.image.load('imgs/enemy.png')

    def update(self, keys):
        self.e_X = self.e_X + self.direcao * self.velocidade
        if self.e_X > 736 or self.e_X < 0:
            self.direcao =  self.direcao * -1
            self.e_Y = self.e_Y + 64 + 4
    def draw(self, screen):
        screen.blit(self.e_IMG, (self.e_X, self.e_Y))
