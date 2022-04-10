import pygame
from Button import Button
from Menus import Menu
from Rounds import Round

class MainGame():
    def __init__(self,screen):
        self.screen = screen
        self.HEIGHT = screen.get_height()
        self.WIDTH = screen.get_width()


    def mainMenu(self):
        menu = Menu(self.screen,["Play","Quit"],"Loop")
        selected_option = menu.outputOptions()
        if selected_option == "Play":
            self.mainLoop()
        else:
            print("See you next time")

    
    def mainLoop(self):
        #
        map_num = 0
        total_maps = 5
        while map_num < total_maps:
            round = Round(self.screen)
        print("rounds and stuff")


if __name__=="__main__":
    screen = pygame.display.set_mode([999,666])
    main = MainGame(screen)
    main.mainMenu()