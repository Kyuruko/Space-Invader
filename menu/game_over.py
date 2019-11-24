import pygame
from menu.highscore import Highscore
from menu.textinput import TextInput

class Game_Over(Highscore):
    def __init__(self):
        super(Game_Over,self).__init__()
        self.bg = pygame.image.load('imgs/game-over.png').convert_alpha()
        self.bg_music = pygame.mixer.music.stop()

        pygame.mixer.music.play(-1)
        self.bg_music_game_over = pygame.mixer.music.load("sounds/game-over.mp3")
        self.textInputBox = TextInput("Digite seu nome:",290,350,200,0)
    
    def update(self,keys,keypress):
        self.name = self.textInputBox.update(keypress)
        if(self.name):
            self.save_score(self.name)
            pygame.mixer.music.stop()
            return "title"
    def draw(self,screen):
        screen.blit(self.bg, (0, 0))
        self.textInputBox.draw(screen)