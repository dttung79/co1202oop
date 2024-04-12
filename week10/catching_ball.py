import pygame
from game import BasicGame
from rectangle import Rectangle
from circle import Circle
import random as rd

class CatchingBall(BasicGame):
    def __init__(self, width, height, speed, bg_color):
        super().__init__(width, height, speed, bg_color)
        self.circle = Circle(width // 2, 0, 10, (255, 0, 255), 5)
        self.rectangle = Rectangle(0, height - 50, 100, 20, (0, 0, 255), 50)
    
    def set_up(self):
        self.n_cicles = 5 # catch 5 circles to win
        self.n_current = 0 # current number of caught circles
    
    def handle_other_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rectangle.move_left()
            elif event.key == pygame.K_RIGHT:
                self.rectangle.move_right(self.window.get_width())
    
    def update(self):
        if self.is_collided():
            self.n_current += 1
            if self.n_current == self.n_cicles:
                self.show_message('You win!')
                # wait for 3 seconds
                pygame.time.wait(3000)
                self.running = False
            # reset the circle position
            self.circle.center_x = rd.randint(0, self.window.get_width())
            self.circle.center_y = 0
        
        if self.is_over():
            self.show_message('You lose!')
            # wait for 3 seconds
            pygame.time.wait(3000)
            self.running = False

        self.circle.move(self.window.get_height())
        self.circle.draw(self.window)
        self.rectangle.draw(self.window)
    
    def is_over(self):
        return self.circle.center_y + self.circle.radius >= self.window.get_height()
    
    def show_message(self, message):
        # clear screen
        self.window.fill(self.bg_color)
        # create font object
        font = pygame.font.Font(None, 36)
        # show message in the center
        text = font.render(message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        self.window.blit(text, text_rect)
        pygame.display.update()

    def is_collided(self):
        leff_collision = self.circle.center_x + self.circle.radius >= self.rectangle.x
        right_collision = self.circle.center_x - self.circle.radius <= self.rectangle.x + self.rectangle.width
        y_collision = self.circle.center_y + self.circle.radius >= self.rectangle.y
        
        if leff_collision and right_collision and y_collision:
                return True
        return False

if __name__ == '__main__':
    game = CatchingBall(800, 600, 60, (255, 255, 255))
    game.run()