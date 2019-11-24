import pygame

class TextInput(pygame.sprite.Sprite):
    def __init__(self, text, xpos, ypos, width, case, maxLength=0, fontSize=22):
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.width = width
        self.initialText = text
        self.case = case
        self.maxLength = maxLength
        self.boxSize = int(fontSize * 1.7)
        self.image = pygame.Surface((width, self.boxSize))
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, width - 1, self.boxSize - 1], 2)
        self.rect = self.image.get_rect()
        self.fontFace = pygame.font.match_font("Arial")
        self.fontColour = pygame.Color("black")
        self.initialColour = (180, 180, 180)
        self.font = pygame.font.Font(self.fontFace, fontSize)
        self.rect.topleft = [xpos, ypos]
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])
        
        self.keypress_cd_timer = 0
        self.keypress_cd_time = 60
        
    def update(self, keyevent):
        self.keypress_cd_timer -= 1
        if(keyevent):
            key = keyevent.key
            if key == pygame.K_RETURN:
               self.clear()
               return self.text
            unicode = keyevent.unicode
            if self.keypress_cd_timer <= 0:
                if key > 31 and key < 127 and (
                        self.maxLength == 0 or len(self.text) < self.maxLength):  # only printable characters
                    if keyevent.mod in (1, 2) and self.case == 1 and key >= 97 and key <= 122:
                        # force lowercase letters
                        self.text += chr(key)
                    elif keyevent.mod == 0 and self.case == 2 and key >= 97 and key <= 122:
                        self.text += chr(key - 32)
                    else:
                        # use the unicode char
                        self.text += unicode

                elif key == 8:
                    # backspace. repeat until clear
                    keys = pygame.key.get_pressed()
                    nexttime = pygame.time.get_ticks() + 200
                    deleting = True
                    while deleting:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_BACKSPACE]:
                            thistime = pygame.time.get_ticks()
                            if thistime > nexttime:
                                self.text = self.text[0:len(self.text) - 1]
                                nexttime = thistime + 50
                                pygame.event.clear()
                        else:
                            deleting = False
                self.keypress_cd_timer = self.keypress_cd_time

    def clear(self):
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width - 1, self.boxSize - 1], 2)
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])
   
    def draw(self,screen):
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width - 1, self.boxSize - 1], 2)
        newSurface = self.font.render(self.text or self.initialText, True, self.fontColour)
        self.image.blit(newSurface, [10, 5])
        screen.blit(self.image,self.rect.topleft)