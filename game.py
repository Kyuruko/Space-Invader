import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet



class Game:
    def __init__(self):
        # game objects
        self.player = Player()
        self.enemy = Enemy()
    def fire(self):
        if Bullet.bullet_cd_timer <= 0:
            Bullet.bullets.append(Bullet(self.player.p_X))
            Bullet.bullet_cd_timer = Bullet.bullet_cd_time

    def update(self, keys):
        Bullet.bullet_cd_timer -= 1
        if keys[pygame.K_SPACE]:
            self.fire()

        # update game objects
        self.player.update(keys)

        for bullet in Bullet.bullets:
            if not bullet.update(keys) or bullet.is_colision(self.enemy):
                Bullet.bullets.remove(bullet)

        self.enemy.update(keys)

    def draw(self, screen):
        from main import background
        screen.blit(background, (0, 0))
        # draw game objects
        self.draw(screen)

        for bullet in Bullet.bullets:
            bullet.draw(screen)

        self.enemy.draw(screen)