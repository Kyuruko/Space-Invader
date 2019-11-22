import pygame


class Bullet:
    def _init_(self, X=0, Y=480):
        self.b_X = X
        self.b_Y = Y

        self.sprite = pygame.image.load('imgs/laser2.png')
        self.W, self.H = self.sprite.get_size()

        bullet_cd_timer = 0
        bullet_cd_time = 120

        self.velocity = -2

        bullets = []

    def update(self, keys):
        # returns false if must be destroyed
        self.b_Y += self.velocity
        if self.b_Y < self.H * -1:
            return False
        return True

    def draw(self, screen):
        screen.blit(self.sprite, (self.b_X, self.b_Y))