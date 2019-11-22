import pygame

class Game_Over:
    def __init__(self):
        self.bg = pygame.image.load('imgs/game-over.png').convert_alpha()
    def update(self, keys):
        if keys[pygame.K_SPACE]:
            return "title"
    def draw(self,screen):
        screen.blit(self.bg, (0, 0))