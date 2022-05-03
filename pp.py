import random
import pygame
from Button import Button


from cmath import cos, sin
import math
from time import time

class Physics:
    going_right = False
    def __init__(self, mass, x_velocity, y_velocity, x, y, frictional_constant, max_speed, terminal_velocity):
        self.mass = mass

        self.max_speed = max_speed
        
        self.terminal_velocity = terminal_velocity
        
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        
        self.x = x
        self.y = y
        
        self.gravity = -9.81
        
        self.frictional_constant = frictional_constant
        
        self.x_displacement = 0
        self.y_displacement = 0
        
        self.time = 1/60

    def planes(self, x_driving_force, y_driving_force, stood_on_rect):
        weight = self.mass * self.gravity
        
        normal_force = 0
        if stood_on_rect:
            normal_force = abs(weight)
            self.y_velocity = 0
            friction = self.frictional_constant * normal_force
        else:
            friction = 0

        y_forces = normal_force + weight + y_driving_force

        a = y_forces/self.mass

        final_y_velocity = self.y_velocity + a*self.time
        
        if final_y_velocity < self.terminal_velocity:
            final_y_velocity = self.terminal_velocity
            print("Terminal Velocity Reached")
        self.y_velocity = final_y_velocity
            
        self.y_displacement = self.y_velocity*self.time - (1/2)*a*self.time**2
        
        #if abs(friction) >= abs(x_driving_force) and self.x_velocity == 0: # stop friction taking maximum value all the time
        #    friction = x_driving_force
            
        if self.x_velocity > 0: # makes friction opose direction of motion
            friction = -friction
        elif self.x_velocity == 0:
            if x_driving_force < 0 and friction > abs(x_driving_force):
                friction = x_driving_force
            elif x_driving_force > 0 and abs(friction) > x_driving_force:
                friction = x_driving_force
            else:
                friction = 0
            
            
        x_forces = friction + x_driving_force

        #print(x_driving_force, -friction)
        
        a = x_forces/self.mass
        #print(a, x_forces, "hello")
        
        final_x_velocity = self.x_velocity + a*self.time
        
        if final_x_velocity > self.max_speed: # stops players being able to accelerate forever
            final_x_velocity = self.max_speed
        elif final_x_velocity < -self.max_speed:
            final_x_velocity = -self.max_speed

        #print(self.x_velocity, final_x_velocity)

        if x_driving_force == 0:
            if self.x_velocity < 0 and final_x_velocity > 0:
                final_x_velocity = 0
            elif self.x_velocity > 0 and final_x_velocity < 0:
                final_x_velocity = 0


        self.x_velocity = final_x_velocity
        
        self.x_displacement = self.x_velocity*self.time - a*self.time**2

        return [(self.x + (self.x_displacement*100), self.y - (self.y_displacement*100)), self.x_velocity, self.y_velocity]



class Game:
    def __init__(self):
        self.screen = pygame.display
        self.screen_rect = self.screen.set_mode((960, 540))
        self.floor = pygame.Rect(0, 350, 960, 100)
        self.floor_co_efficient = 0.55
        self.mass = 65
        self.man = pygame.Rect(0, 0, 50, 100)
        self.terminal_velocity = -math.sqrt((2*self.mass*9.81)/(1000*0.1*0.12))
        print("Terminal Velocity = ", self.terminal_velocity," m/s and", (self.terminal_velocity*62)," pixels")
        self.extended_man = pygame.Rect(0, 0, 50, 1)
        self.extended_man.topleft = self.man.bottomleft
        self.max_speed = 0
        self.sprint_max_speed = 350
        self.walk_max_speed = 200
        self.x_velocity = 0
        self.y_velocity = 0
        self.clock = pygame.time.Clock()

    def display(self):
        run = True
        SPRINT_FORCE = 600
        MOVE_FORCE = 400
        JUMP_FORCE = 19000
        while run:
            
            self.on_rect = False
            print(self.man.bottomleft)
            if self.extended_man.colliderect(self.floor):
                self.on_rect = True
                if self.man.colliderect(self.floor):
                    self.man.bottomleft = (self.man.bottomleft[0], self.floor.topleft[1])
                    self.extended_man.topleft = self.man.bottomleft 
            
            self.screen.update()
            
            key = pygame.key.get_pressed()
        
            self.clock.tick(60)
            self.x_driving_force = 0
            self.y_driving_force = 0
            self.screen_rect.fill((100, 100, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #and self.on_rect:
                        self.y_driving_force = JUMP_FORCE
                        print("please stop ignore\n\n\n\n\n\n\n\n\n\n\n")
                        
            if key[pygame.K_LSHIFT]:
                sprint = True
                self.max_speed = self.sprint_max_speed
            else:
                sprint = False
                self.max_speed = self.walk_max_speed
            
            if key[pygame.K_d]:#moving right
                if sprint:
                    self.x_driving_force = SPRINT_FORCE
                else:
                    self.x_driving_force = MOVE_FORCE
            if key[pygame.K_a]:#moving left
                if sprint:
                    self.x_driving_force = -SPRINT_FORCE
                else:
                    self.x_driving_force = -MOVE_FORCE


            pygame.draw.rect(self.screen_rect, (100, 0, 0), self.floor)
            pygame.draw.rect(self.screen_rect, (0, 50, 50), self.man)

            p = Physics(self.mass, self.x_velocity, self.y_velocity, self.man.topleft[0], self.man.topleft[1], self.floor_co_efficient, self.max_speed, self.terminal_velocity)

            info = p.planes(self.x_driving_force, self.y_driving_force, self.on_rect)

            self.man.topleft = info[0]
            self.extended_man.topleft = self.man.bottomleft
            self.x_velocity = info[1]
            self.y_velocity = info[2]

g = Game()
g.display()
        
