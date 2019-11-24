import pygame
from cores import YELLOW
from menu.highscore import Highscore

class ShowScore(Highscore):
    def __init__(self):
        super(ShowScore,self).__init__()
        self.bg = pygame.image.load('imgs/menu-bg.png').convert_alpha()
        
        self.scroller = pygame.Surface((400,400))
        self.font = pygame.font.Font("fonts/times.ttf", 24)
        
        for i,player_score in enumerate(self.player_scores):
            name = player_score["name"]
            score = player_score["score"]
            scorestr=name+": "+str(score)
            self.text = self.font.render(scorestr, True, YELLOW)
            self.scroller.blit(self.text,(0,24*i))
        
    def update(self,keys,keyevent):
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
               return "title"
    
    def draw(self,screen):
        screen.blit(self.bg,(0,0))
        screen.blit(self.scroller,(200,150))