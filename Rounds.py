from Characters import *

class Round():
    def __init__(self,screen):
        self.screen = screen
        player_image = "nothing"
        self.player = Player(self.screen,[player_image])
        self.entities = pygame.sprite.Group()
    def mainLoop(self):
        pass
        #check player movements and stuff
        #-
        #handle groups of players and ghosts
        