import random
import pygame

class Bolide:
    def __init__(self,name,speed, skill, strategy, colour):
        self.name = name
        self.speed = speed
        self.skill = skill
        self.strategy = strategy
        self.position = 0
        self.lap_time = 0
        self.colour = colour
        

    def update_position(self, lap_length):
        pass  

    def draw(self, screen):
        pass  
