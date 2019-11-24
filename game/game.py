import pygame
from game.player import Player
from game.enemy import Enemy, Enemies
from game.bullet import Bullet
from menu.hud import HUD


class Game:
    def __init__(self):
        self.bg = pygame.image.load('imgs/game-bg.png')
        # variavel que determina a velocidade de tiro
        self.bullet_cd_timer = 0
        self.bullet_cd_time = 60
        self.bullets = []

        # game objects
        self.player = Player()
        self.enemy = Enemies()
        self.hud = HUD()

    # funçao que determina o intervalo entre um tiro e outro
    def fire(self):
        if self.bullet_cd_timer <= 0:
            self.bullets.append(Bullet(self.player.p_X))
            self.bullet_cd_timer = self.bullet_cd_time

    # funcao que faz a açao de atirar
    def update(self, keys,keypress):
        self.bullet_cd_timer -= 1
        if keys[pygame.K_SPACE]:
            self.fire()

        # atualiza na tela os objetos
        self.player.update(keys)

        # some o tiro caso n atinja ninguém
        for bullet in self.bullets:
            if not bullet.update(keys):
                self.bullets.remove(bullet)
                return
            # some o tiro caso atinja o inimigo
            if self.enemy.collision_bullet(bullet):
                self.bullets.remove(bullet)
                self.hud.add_score()
        # funçao que determina o fim de jogo
        if self.enemy.collision_pve(self.player):
            return 'game-over'
        self.hud.update(keys)
        if self.enemy:
            self.enemy.update(keys)

    # aparece o HUD na tela
    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        self.hud.draw(screen)

        # desenha o inimigo e a bala na tela
        for bullet in self.bullets:
            bullet.draw(screen)
        self.player.draw(screen)
        if self.enemy:
            self.enemy.draw(screen)