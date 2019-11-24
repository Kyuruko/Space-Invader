import pygame

class Title:
    def __init__(self):
        self.bg = pygame.image.load('imgs/menu-bg.png').convert_alpha()
      
        #"novo jogo"
        self.newgame1 = pygame.image.load('imgs/menu-novo1.png')
        self.newgame2 = pygame.image.load('imgs/menu-novo2.png')
        
        #"tabela de pontuação"
        self.highscore1 = pygame.image.load('imgs/menu-tabela1.png')
        self.highscore2 = pygame.image.load('imgs/menu-tabela2.png')
        
        #"sair"
        self.exit1 = pygame.image.load('imgs/menu-sair1.png')
        self.exit2 = pygame.image.load('imgs/menu-sair2.png')
        
        #delay para mudança de opçao do menu, se não o menu fica doido
        self.timer=10
        self.delay=5
        
        self.selected = 0
        
        # o que deve ser chamado em cada posiçao
        self.actions=["game","show-score","exit"]
    def update(self,keys,keypress):
        if self.selected < 0: 
            self.selected = 2
        if self.selected > 2:
            self.selected = 0
        self.timer-=1
        
        
        if self.timer <=0:
           if keys[pygame.K_UP]:
                self.selected-=1
                self.timer = self.delay
           if keys[pygame.K_DOWN]:
                self.selected+=1
                self.timer = self.delay
 
           if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
               return self.actions[self.selected]
        
    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        
        if self.selected == 0:
            screen.blit(self.newgame2, (0, 0))
        else:
            screen.blit(self.newgame1, (0, 0))
            
            
        if self.selected == 1:
           screen.blit(self.highscore2, (0, 0))
        else:
           screen.blit(self.highscore1, (0, 0))
            
            
        if self.selected == 2:
           screen.blit(self.exit2, (0, 0))
        else:
           screen.blit(self.exit1, (0, 0))
        