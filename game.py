import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet



class Game:
    def __init__(self):
        self.bg = pygame.image.load('imgs/game-bg.png')

        self.bullet_cd_timer = 0
        self.bullet_cd_time = 120
        self.bullets = []

        # game objects
        self.player = Player()
        self.enemy = Enemy()
    def fire(self):
        if self.bullet_cd_timer <= 0:
            self.bullets.append(Bullet(self.player.p_X))
            self.bullet_cd_timer = self.bullet_cd_time

    def update(self, keys):
        self.bullet_cd_timer -= 1
        if keys[pygame.K_SPACE]:
            self.fire()

        # update game objects
        self.player.update(keys)

        for bullet in self.bullets:
            if not bullet.update(keys) or bullet.is_colision(self.enemy):
                self.bullets.remove(bullet)

        self.enemy.update(keys)

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        # draw game objects
        self.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)

        self.enemy.draw(screen)