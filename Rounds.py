from Characters import *

class Round():
    def __init__(self,screen):
        self.screen = screen
        player_image = "nothing"
        self.player = Player(self.screen,[player_image])
    def mainLoop(self):
        print("player stuff")
        print("move the map")
        #handle groups of players and ghosts
        