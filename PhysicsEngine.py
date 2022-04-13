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

    '''
    
Even though it looks shit it should probably work after ive fixed some small errors

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

        for i in range(1,45):
            x_pos = final_x_vel - initial_x_vel / 2*self.acceleration
            y_pos = final_y_vel - initial_y_vel / 2*self.acceleration
            x_points.append(x_pos)
            y_points.append(y_pos)
            final_x_vel = initial_x_vel
            final_y_vel = initial_y_vel
            initial_x_vel = initial_x_vel - frame_seperation
            initial_x_vel = initial_x_vel - frame_seperation
            y_spd = y_spd - frame_seperation
            if y_spd == 0:
                for i in range(1,45):
                    x_difference = x_points[i] - x_points[i - 1]
                    y_difference = x_points[i] - x_points[i - 1]
                    x_pos = x_pos + x_difference
                    y_pos = y_pos - y_difference
                    self.x = original_x + x_pos
                    self.y = original_y + y_pos
                    player_pos = (math.trunc(self.x),math.trunc(self.y))
                    return player_pos
            self.x = original_x + x_pos
            self.y = original_y + y_pos
            player_pos = (math.trunc(self.x),math.trunc(self.y))
            return player_pos








