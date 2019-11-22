import pygame
import os


class Player:
    def __init__(self):
        self.p_X = 370
        self.p_Y = 480

        self.velocidade = 1

        self.p_IMG = pygame.image.load('imgs/nave.png')

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.p_X += -self.velocidade
        if keys[pygame.K_RIGHT]:
            self.p_X += self.velocidade

        if self.p_X <= 0:
            self.p_X = 0
        elif self.p_X >= 736:
            self.p_X = 736

    def draw(self, screen):
        screen.blit(self.p_IMG, (self.p_X, self.p_Y))
