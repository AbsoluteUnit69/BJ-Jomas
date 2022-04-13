from cmath import cos, sin
import math
from time import time

class Physics:
    def __init__(self,mass,velocity,set_speed,x,y,gravity,angle,frictional_constant):
        self.mass =  mass
        self.velocity = velocity
        self.set_speed = set_speed
        self.x = x
        self.y = y
        self.speed = abs(self.velocity)
        self.gravity = gravity
        self.momentum = self.mass * self.speed
        self.frictional_constant = frictional_constant
        self.angle = angle
        self.displacement = 0

    '''
    
Even though it looks shit it should probably work after ive fixed some small errors

hopefully at least

ignore first two functions just keepin em for a bit to track my progress cus who knows if any of what i have done is right 
probably not though lmao :'(

'''
    
    def jumpPoints(self):
        frame_seperation = self.speed / 45
        original_x = self.x
        original_y = self.y
        x_vel = self.velocity*cos(self.angle)
        y_vel = self.speed*sin(self.angle)
        initial_x_vel = x_vel
        initial_y_vel = y_vel
        final_x_vel = initial_x_vel - frame_seperation
        final_y_vel = initial_y_vel - frame_seperation
        x_points = []
        y_points = []
        y_spd = self.speed
        while y_spd != 0:
            x_pos = pow(final_x_vel,2) - pow(initial_x_vel,2) / 2*self.gravity
            y_pos = pow(final_y_vel,2) - pow(initial_y_vel,2) / 2*self.gravity
            x_points.append(x_pos)
            y_points.append(y_pos)
            final_x_vel = initial_x_vel
            final_y_vel = initial_y_vel
            initial_x_vel = initial_x_vel - frame_seperation
            initial_x_vel = initial_x_vel - frame_seperation
            y_spd = y_spd - frame_seperation
            self.x = original_x + x_pos
            self.y = original_y + y_pos
            player_pos = (math.trunc(self.x),math.trunc(self.y))
            print(player_pos)

        for i in range(0,45):
            x_difference = x_points[45-i] - x_points[45-i+1]
            y_difference = x_points[i] - x_points[i - 1]
            x_pos = x_pos + x_difference
            y_pos = y_pos - y_difference
            self.x = original_x + x_pos
            self.y = original_y + y_pos
            player_pos = (math.trunc(self.x),math.trunc(self.y))
            print(player_pos)

    def newJump(self):
        original_y = self.y
        original_x = self.x
        total_jump_time = 1.5 #seconds
        frames = 90
        x_speed = self.velocity*cos(self.angle)
        y_initial_velocity = self.speed*sin(self.angle)
        time_per_frame = total_jump_time / frames
        for i in range(0,frames):
            y_displacement = y_initial_velocity*time + self.gravity*time**2
            x_distance = x_speed*time
            y_final_velocity = y_initial_velocity + self.gravity*time
            y_initial_velocity = y_final_velocity
            time = time + time_per_frame
            self.y = math.trunc(original_y + y_displacement)
            self.x = math.trunc(original_x + x_distance)
            player_pos = (self.x,self.y)

    def jump(self):
        original_y = self.y
        original_x = self.x
        x_speed = self.velocity*cos(self.angle)
        y_initial_velocity = self.speed*sin(self.angle)
        time_frame = 0.1
        time = 0
        not_colliding = True
        while not_colliding:
            y_displacement = y_initial_velocity*time + self.gravity*time**2
            x_distance = x_speed*time
            y_final_velocity = y_initial_velocity + self.gravity*time
            y_initial_velocity = y_final_velocity
            time = time + time_frame
            self.y = math.trunc(original_y + y_displacement)
            self.x = math.trunc(original_x + x_distance)
            player_pos = (self.x,self.y)
            if player_pos == 69:    # need some thing here so if he lands on/hits something it stops but otherwise keeps going e.g. if the player over shoots or undershoots a platform
                not_colliding = False

    def planes(self):
        weight = self.mass * self.gravity
        normal_force = weight
        friction = self.frictional_constant * normal_force
        self.velocity = self.set_speed - friction


    def inclinedPlanes(self):
        pass

            










