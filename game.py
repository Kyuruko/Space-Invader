import pygame
from player import Player
from enemy import Enemy, Enemies
from bullet import Bullet
from hud import HUD


class Game:
    def __init__(self):
        self.bg = pygame.image.load('imgs/game-bg.png')

        self.bullet_cd_timer = 0
        self.bullet_cd_time = 60
        self.bullets = []

        # game objects
        self.player = Player()
        self.enemy = Enemies()
        self.hud = HUD()
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
            if not bullet.update(keys):
                self.bullets.remove(bullet)
                return
            if self.enemy.collision_bullet(bullet):
                self.bullets.remove(bullet)
                self.hud.add_score()
        if self.enemy.collision_pve(self.player):
            return 'game-over'
        self.hud.update(keys)
        if self.enemy:
            self.enemy.update(keys)
    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        self.hud.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)
        self.player.draw(screen)
        if self.enemy:
            self.enemy.draw(screen)