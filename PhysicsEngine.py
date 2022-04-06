import math

class Particle:
    def __init__(self,mass,velocity,x,y,acceleration):
        self.mass =  mass
        self.velocity = velocity
        self.x = x
        self.y = y
        self.speed = abs(self.velocity)
        self.acceleration = acceleration
        self.momentum = self.mass * self.speed

    
