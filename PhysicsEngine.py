from cmath import cos, sin
import math

class Particle:
    def __init__(self,mass,velocity,x,y,acceleration,angle):
        self.mass =  mass
        self.velocity = velocity
        self.x = x
        self.y = y
        self.speed = abs(self.velocity)
        self.acceleration = 9.81
        self.momentum = self.mass * self.speed
        self.angle = angle
        self.displacement = 0
    
    def jump(self):
        player_pos = ""
        frame_seperation = self.speed / 45
        original_x = self.x
        original_y = self.y
        x_vel = self.velocity*cos(self.angle)
        y_vel = self.speed*sin(self.angle)
        initial_x_vel = x_vel
        initial_y_vel = y_vel
        final_x_vel = initial_x_vel - frame_seperation
        final_y_vel = initial_y_vel - frame_seperation

        for i in range(1,45):
            x_pos = final_x_vel - initial_x_vel / 2*self.acceleration
            y_pos = final_y_vel - initial_y_vel / 2*self.acceleration
            final_x_vel = initial_x_vel
            final_y_vel = initial_y_vel
            initial_x_vel = initial_x_vel - frame_seperation
            initial_x_vel = initial_x_vel - frame_seperation
            if initial_y_vel == 0:
                pass

            player_pos = (x_pos,y_pos)
            return player_pos







