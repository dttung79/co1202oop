import pygame
from abc import ABC, abstractmethod

class BasicGame(ABC):
    def __init__(self, width, height, speed, bg_color):
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.speed = speed
        self.bg_color = bg_color
    
    def run(self):
        self.set_up()
        self.running = True
        while self.running:
            self.window.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.handle_other_events(event)
            self.update()
            pygame.display.update()
            self.clock.tick(self.speed)
        pygame.quit()
    
    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def handle_other_events(self, event):
        pass

    @abstractmethod
    def update(self):
        pass