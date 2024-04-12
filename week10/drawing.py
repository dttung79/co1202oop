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

    def draw_rect(self, x, y, width, height, color):
        pygame.draw.rect(self.window, color, (x, y, width, height))

    def run(self):
        running = True
        x = 100
        y = 100
        step = 5
        # main loop to keep the game running
        while running:
            # fill the window with white color
            self.window.fill((255, 255, 255))
            # waiting for events, if event is quit then stop the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x -= step
                    elif event.key == pygame.K_RIGHT:
                        x += step
                    elif event.key == pygame.K_UP:
                        y -= step
                    elif event.key == pygame.K_DOWN:
                        y += step
            # draw a rectangle at position (100, 100) with width 50 and height 50, red color
            self.draw_rect(x, y, 50, 50, (255, 0, 0))
            # update the screen
            pygame.display.update()
            # then wait for a while
            self.clock.tick(self.speed)
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()