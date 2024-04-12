import pygame

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Create game window
        self.window = pygame.display.set_mode((800, 600))
        # Set game speed
        self.clock = pygame.time.Clock()
        self.speed = 60
    
    def draw_circle(self, center_x, center_y, radius, color):
        pygame.draw.circle(self.window, color, (center_x, center_y), radius)

    def run(self):
        direction = True # True is falling, False is rising
        x = self.window.get_width() // 2
        y = self.window.get_height() // 2
        running = True
        radius = 50
        speed = 10
        moving = False

        while running:
            self.window.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        moving = not moving
            if moving:
                if direction:
                    y += speed
                    if y >= self.window.get_height() - radius:
                        direction = False
                else:
                    y -= speed
                    if y <= radius:
                        direction = True
            self.draw_circle(x, y, radius, (255, 0, 255))
            pygame.display.update()
            self.clock.tick(self.speed)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()