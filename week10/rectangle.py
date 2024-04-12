import pygame
class Rectangle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
    
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
    
    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    
    def move_right(self, max_x):
        if self.x < max_x - self.width:
            self.x += self.speed