from Characters import *

class Round():
    def __init__(self,screen):
        self.screen = screen
        player_image = "player.png"
        self.ghost_image = "ghost.png"
        self.player = Player(self.screen,player_image)
        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)
        self.map = self.getMap()

        self.FPS = 60
        self.clock = pygame.time.Clock()
    def getMap(self):
        pass    
    def mainLoop(self):
        self.screen.fill((0,0,0))
        self.map.display(self.screen)
        self.entities.update(self.map)
        self.handlePlayerActions()
        #check player movements and stuff
        #move around the sprites
        #handle player interactions
        self.screen.flip()
        self.clock.tick(self.FPS)
    def handlePlayerActions(self):
        if not self.player.isDoingAction():
            return
        if self.player.isStartingLoop():
            self.initialLoopCoords = self.player.getCoords()
            self.map.setRespawn()
            self.original_map_state = self.map.getMapState()
            self.player.startCollectingCoords()
            self.player.startCollectingInteractions()
            self.handleAnimation()
            
        if self.player.isEndingLoop():
            self.player.stopCollectingCoords()
            self.player.stopCollectingActions()
            self.handleAnimation()
        if self.player.isEndingLoopCycle():
            coords = self.player.getCollectedCoords()
            actions = self.player.getCollectedActions()
            self.player.resetCoordCollection()
            self.player.resetActionCollection()
            ghost = Ghost(self.screen,self.ghost_image,coords,actions)
            self.entities.add(ghost)
            self.player.setCoords(self.initialLoopCoords)
            self.entities.reset()
            self.map = self.original_map_state
        if self.player.isInteracting():
            pass
        if self.player.isBoosting():
            self.map.setBoostLocation()
            self.handleAnimation()
    def handleAnimation(self):
        pass #leave to freddie - he loves this kinda thing          no i dont
        