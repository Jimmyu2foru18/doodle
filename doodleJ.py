# doodle.py
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the drawing window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Doodle Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up drawing variables
drawing = False
last_pos = None
color = BLACK
radius = 5

# Fill the background with white
screen.fill(WHITE)

# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        elif event.type == pygame.KEYDOWN:
            # Change color based on key press
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                radius += 1
            elif event.key == pygame.K_MINUS:
                radius = max(1, radius - 1)

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos is not None:
            pygame.draw.line(screen, color, last_pos, mouse_pos, radius * 2)
        last_pos = mouse_pos

    # Update the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
sys.exit()