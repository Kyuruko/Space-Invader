import pygame


class Bullet:
    def __init__(self, X=0, Y=480):
        self.b_X = X
        self.b_Y = Y

        self.b_IMG = pygame.image.load('imgs/laser2.png')
        self.W, self.H = self.b_IMG.get_size()

        self.velocity = -8

    def update(self, keys):
        # returns false if must be destroyed
        self.b_Y += self.velocity
        if self.b_Y < self.H * -1:
            return False
        return True

    def draw(self, screen):
        screen.blit(self.b_IMG, (self.b_X, self.b_Y))