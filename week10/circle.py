import pygame

class Circle:
    def __init__(self, center_x, center_y, radius, color, speed):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.speed = speed
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.center_x, self.center_y), self.radius)
    
    def move(self, max_y):
        if self.center_y < max_y - self.radius:
            self.center_y += self.speed