import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
from hud import HUD


class Game:
    def __init__(self):
        self.bg = pygame.image.load('imgs/game-bg.png')

        self.bullet_cd_timer = 0
        self.bullet_cd_time = 120
        self.bullets = []

        # game objects
        self.player = Player()
        self.enemy = Enemy()
        self.hud = HUD()
    def fire(self):
        if self.bullet_cd_timer <= 0:
            self.bullets.append(Bullet(self.player.p_X))
            self.bullet_cd_timer = self.bullet_cd_time

    def collision_pve(self):
        if self.player.p_X < self.enemy.e_X + 64 and self.player.p_X + 64 > self.enemy.e_X and self.player.p_Y < self.enemy.e_Y + 64 and self.player.p_Y + 64 > self.enemy.e_Y:
            return True
        return False

    def collision_bullet(self, bullet):
        if bullet.b_X < self.enemy.e_X + 48 and bullet.b_X + 48 > self.enemy.e_X and bullet.b_Y < self.enemy.e_Y + 64 and bullet.b_Y + 64 > self.enemy.e_Y:
            return True
        return False

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
            if self.collision_bullet(bullet):
                self.enemy = Enemy()
                self.bullets.remove(bullet)
                self.hud.add_score()
        if self.collision_pve():
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