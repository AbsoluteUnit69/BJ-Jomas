from cmath import acos, asin, cos, sin
import math
import pygame
import pymunk
import pymunk.pygame_util
from time import time

class Particle:
    def __init__(self,mass,velocity,x,y,acceleration,angle,time):
        self.mass =  mass
        self.velocity = velocity
        self.x = x
        self.y = y
        self.speed = abs(self.velocity)
        self.acceleration = acceleration
        self.momentum = self.mass * self.speed
        self.angle = angle


    def jump(self):
        total_time = 1.5
        total_frames = 90
        frame_time = total_time/total_frames
        for i in range(1,total_frames):
            time = frame_time*i
            self.x = cos(self.angle)*(self.velocity*time)+(self.acceleration*pow(time,2)/2)
            self.y = sin(self.angle)*(self.velocity*time)+(self.acceleration*pow(time,2)/2)


    
