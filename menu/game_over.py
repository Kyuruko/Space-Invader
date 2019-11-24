import pygame

class Game_Over:
    def __init__(self):

        self.bg = pygame.image.load('imgs/game-over.png').convert_alpha()
        self.bg_music = pygame.mixer.music.stop()

        self.bg_music_game_over = pygame.mixer.music.load("sounds/game-over.mp3")
        pygame.mixer.music.play(-1)

    # funcao que reseta a tela de GO, para o menu principal
    def update(self, keys):
        if keys[pygame.K_r]:
            pygame.mixer.music.stop()
            return "title"

    # desenha a tela de GO
    def draw(self,screen):
        screen.blit(self.bg, (0, 0))