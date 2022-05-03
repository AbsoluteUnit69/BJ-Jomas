import pygame
from pp import *

class Character(pygame.sprite.Sprite):
    def __init__(self,screen,image):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.horizontal_speed = 0
        self.vertical_speed = 0
        self.horizontal_accel = 0
        self.vertical_accel = 0
        self.mass = 60
        self.jumping = False

    def output(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        pass
        #handle outputting character
    def reset(self):
        pass
class Player(Character):
    def __init__(self,screen,image):
        super().__init__(screen,image)
        self.saved_coords = []
        self.saved_actions = []
        self.max_cycles = 5
    def findNextPos(self,map):
        returned_data = Physics.planes(self.physics,self.x_drving_force,self.y_driving_force,self.on_rect)#[(self.x + (self.x_displacement*100), self.y - (self.y_displacement*100)), self.x_velocity, self.y_velocity]
        next_coords = (returned_data[0],returned_data[1])
        temp_rect = self.image.get_rect()
        temp_rect.center = next_coords
        collision = map.checkCollisions(temp_rect)
        if not collision:
            self.rect.center = next_coords
            self.x_velocity = returned_data[2]
            self.y_velocity = returned_data[3]

    def movement(self,map):
        JUMP_SPEED = 3
        MOVE_SPEED = 2
        SPRINT_SPEED = 4

        key = pygame.key.get_pressed()
        if key[pygame.K_LSHIFT]:
            sprint = True
        else:
            sprint = False
        if key[pygame.K_w] or key[pygame.K_SPACE] and not self.jumping:#jumping 
            self.jumping = True
            self.vertical_speed = JUMP_SPEED
            self.vertical_accel = -9.81

        self.x_driving_force = 0
        if key[pygame.K_d]:#moving right
            if sprint:
                self.x_driving_force += SPRINT_SPEED
            else:
                self.x_driving_force += MOVE_SPEED     
        if key[pygame.k_a]:#moving left
            if sprint:
                self.x_driving_force -= SPRINT_SPEED
            else:
                self.x_driving_force -= MOVE_SPEED

        self.findNextPos(map)
    def interactions(self,map):
        if self.looping:
            self.loop_timer -=1
            if self.loop_timer < 0:
                self.ending_cycle = True
                self.doing_action = True
                self.cycles+=1
                action = "ending cycle"
        key = pygame.key.get_pressed()
        if key[pygame.K_e] and not self.doing_action and not self.looping:#starting the loop
            self.starting_loop = True
            self.doing_action = True
            self.looping = True
            self.loop_timer = 300
            self.cycles = 0
            action = "starting loop"
        if key[pygame.k_q] and not self.doing_action:#ending the loop and all ghosts come back to player
            self.ending_loop = True
            self.doing_action = True
            self.looping = False
            action = "ending loop"
        if key[pygame.k_r] and not self.doing_action:#ending the current cycle, and looping back to create ghost
            self.ending_cycle = True
            self.doing_action = True
            self.cycles+=1
            action = "ending cycle"
        if key[pygame.k_f] and not self.doing_action:#interacting with stuff, like levers etc
            interacted = map.checkInteractions(self.rect)
            if interacted:
                self.interacting_full = True
            else:
                self.interacting = True
            self.doing_action = True
            action = "interacting"
        if key[pygame.K_TAB] and not self.doing_action:#boosting someone into the air
            self.boost = True
            self.doing_action = True
            action = "boosting"
        
        if self.cycles ==self.max_cycles:
            self.ending_cycle = False
            self.looping = False
            self.ending_loop = True
            self.doing_action = True
            action = "ending loop"
        if self.collecting_actions:
            self.saved_actions.append(action)
    def handleAnimations(self):
        pass # leave to freddie
    def update(self,map):
        self.movement(map)
        self.interactions(map)
        self.handleAnimations()
        self.output()

        if self.collecting_coords:
            self.saved_coords.append(self.rect.center)
    def startCollectingCoords(self):
        self.collecting_coords = True
    def resetCoordCollection(self):
        self.saved_coords = []
    def stopCollectingCoords(self):
        self.collecting_coords = False
    def startCollectingActions(self):
        self.collecting_actions = True
    def resetActionCollection(self):
        self.saved_actions = []
    def stopCollectingActions(self):
        self.collecting_actions = False
    #setters:

    #getters:
    def isDoingAction(self):
        return self.doing_action
    def isStartingLoop(self):
        return self.starting_loop
    def isEndingLoop(self):
        return self.ending_loop
    def isEndingLoopCycle(self):
        return self.ending_cycle
    def isInteracting(self):
        return (self.interacting_full or self.interacting)
    def isBoosting(self):
        return self.boost
    def getCoords(self):
        return self.rect.center
    def isLooping(self):
        return self.looping
class Ghost(Character):
    def __init__(self,screen,image,coords,actions):
        super().__init__()
        self.coords_list = coords
        self.actions_list = actions
        self.current_frame = 0
    def movement(self,map):
        current_coord = self.coords_list[self.current_frame]
        current_action = self.actions_list[self.current_frame]
        self.rect.center = current_coord
        if current_action == "starting loop":#starting the loop
            self.starting_loop = True
            self.looping = True
        if current_action == "ending loop":#ending the loop and all ghosts come back to player
            self.ending_loop = True
        if current_action == "ending cycle":#ending the current cycle, and looping back to create ghost
            self.ending_cycle = True
        if current_action == "interacting":#interacting with stuff, like levers etc
            interacted = map.checkInteractions(self.rect)
            if interacted:
                self.interacting_full = True
            else:
                self.interacting = True
        if current_action == "boosting":#boosting someone into the air
            self.boost = True
    def handleAnimations(self):
        pass #leave for freddie
    def update(self,map):
        if self.current_frame < len(self.coords_list)-1:
            self.movement(map)
            self.handleAnimations()
            self.current_frame +=1
        else:
            pass # basically removes all functionality of the ghost since theres nothing there anymore
    def reset(self):
        self.current_frame = 0
        
        #just has to move along with the coords its given

