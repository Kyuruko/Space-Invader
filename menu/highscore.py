from menu.hud import HUD
import pygame

highscore_file_name = "high-score.txt"
class Highscore:
    def __init__(self):        
        self.player_scores = self.load_score()
        self.score = HUD.score        
        
    def load_score(self):
        player_scores=[]
        # abre o a arquivo de score para ler as linhas
        score_file = open(highscore_file_name, "r")
        for entry in score_file:
           name,score = entry.split(":")
           player_scores.append({"score":int(score),"name":name})
        # fecha o arquivo de score
        score_file.close()
        return player_scores
         
       
    def save_score(self,name):
        # adiciona o score na lista
        self.player_scores.append({"score":self.score,"name":name})
        self.sort_score()
        # limpa o arquivo de score
        open(highscore_file_name, "w").close()
        
        # abre o arquivo para adicionar linhas
        score_file = open(highscore_file_name, "a")
       
        for player_score in self.player_scores:
            score_file.write(player_score["name"]+":"+str(player_score["score"])+"\n")
        
        # fecha o arquivo de score
        score_file.close()

    def sort_score(self):
        # ordena a lista de score de acordo com o score do player
        self.player_scores.sort(key = lambda player_score:player_score["score"])
        
    def update(self,keys):
        pass
        
    def draw(self, screen):
        screen.blit(self.hd_bg, (0,0))                                                                