import pygame
from PhysicsEngine import Particle

class Character(pygame.sprite.Sprite):
    def __init__(self,screen,image):
        super().__init__()
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
class Player(Character):
    def __init__(self):
        super().__init__()
    def findNextPos(self,map):
        next_coords = PhysicsEngine.SomeMethod()
        temp_rect = self.image.get_rect()
        temp_rect.center = next_coords
        collision = map.checkCollisions(temp_rect)
        if not collision:
            self.rect.center = next_coords

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

        self.driving_force = 0
        if key[pygame.K_d]:#moving right
            if sprint:
                self.driving_force += SPRINT_SPEED
            else:
                self.driving_force += MOVE_SPEED     
        if key[pygame.k_a]:#moving left
            if sprint:
                self.driving_force -= SPRINT_SPEED
            else:
                self.driving_force -= MOVE_SPEED

        self.findNextPos(map)
    def interactions(self,map):
        key = pygame.key.get_pressed()
        if key[pygame.K_e] and not self.doing_action:#starting the loop
            self.starting_loop = True
            self.doing_action = True
        if key[pygame.k_q] and not self.doing_action:#ending the loop and all ghosts come back to player
            self.ending_loop = True
            self.doing_action = True
        if key[pygame.k_r] and not self.doing_action:#ending the current cycle, and looping back to create ghost
            self.looping = True
            self.doing_action = True
        if key[pygame.k_f] and not self.doing_action:#interacting with stuff, like levers etc
            interacted = map.checkInteractions()
            if interacted:
                self.interacting_full = True
            else:
                self.interacting = True
            self.doing_action = True
        if key[pygame.K_TAB] and not self.doing_action:#boosting someone into the air
            self.boost = True
    def update(self,map):
        self.movement(map)
        self.interactions(map)
        self.output()

class Ghost(Character):
    def __init__(self):
        super().__init__()
    
    def update(self,map):
        pass

