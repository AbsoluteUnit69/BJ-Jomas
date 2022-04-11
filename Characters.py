import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self,screen,image):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()

    def update(self):
        pass
        #handle outputting character
class Player(Character):
    def __init__(self):
        super().__init__()
    
    def update(self):
        pass
        #handle outputting player
        #handle movement
        #handle player interactions

class Ghost(Character):
    def __init__(self):
        super().__init__()

