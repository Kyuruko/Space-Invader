from menu.highscore import Highscore
from menu.textinput import TextInput

class AddScore(Highscore):
    def __init__(self):
        super(AddScore,self).__init__()
        self.textInputBox = TextInput("Digite seu nome",310,300,120,0)
    def update(self,keys,keypress):
        self.name = self.textInputBox.update(keypress)
        if(self.name):
            self.save_score(self.name)
            return "title"
    def draw(self,screen):
        self.textInputBox.draw(screen)