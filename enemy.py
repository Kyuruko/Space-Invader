import pygame
import random
from bullet import Bullet
from player import Player


class Enemy:
    def __init__(self):
        self.e_X = random.randint(0, 400)
        self.e_Y = random.randint(50, 150)

        self.velocidade = 1
        self.direcao = 1

        self.e_IMG = pygame.image.load('imgs/enemy.png')

        self.player = Player()
        self.bullet = Bullet()

    def update(self, keys):
        self.e_X = self.e_X + self.direcao * self.velocidade
        if self.e_X > 736 or self.e_X < 0:
            self.direcao = self.direcao * -1
            self.e_Y = self.e_Y + 64 + 4

    def draw(self, screen):
        screen.blit(self.e_IMG, (self.e_X, self.e_Y))

    def respawn(self):
        self.e_X = random.randint(0, 400)
        self.e_Y = random.randint(50, 150)
        self.velocidade += 0.25
        self.player.velocidade = 0.05
        self.bullet.velocity = -0.10



class Enemies:
    def __init__(self):

        enemy = Enemy()

        self.bullet = Bullet()

        self.num_enemy = 6
        self.enemies = []
        for i in range(self.num_enemy):
            self.enemies.append(Enemy())

    def update(self, keys):
        for i in range(self.num_enemy):
            self.enemies[i].update(keys)

    def draw(self, screen):
        for i in range(self.num_enemy):
            self.enemies[i].draw(screen)

    def collision_pve(self, player):
        for enemy in self.enemies:
            if player.p_X < enemy.e_X + 64 and player.p_X + 64 > enemy.e_X and player.p_Y < enemy.e_Y + 64 and player.p_Y + 64 > enemy.e_Y:
                return True
        return False

    def collision_bullet(self, bullet):
        for enemy in self.enemies:
            if bullet.b_X < enemy.e_X + 48 and bullet.b_X + 48 > enemy.e_X and bullet.b_Y < enemy.e_Y + 48 and bullet.b_Y + 64 > enemy.e_Y:
                enemy.respawn()
                return True
        return False
