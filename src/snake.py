import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Set the initial snake position and size
snake = [(200, 200), (210, 200), (220, 200)]
snake_color = (255, 0, 0)
snake_size = 10

# Set the initial food position and size
food = (random.randint(0, 800), random.randint(0, 600))
food_color = (0, 255, 0)
food_size = 10

# Set the initial velocity of the snake
velocity_x = 0.5
velocity_y = 0

# Initialize the score
score = 0

# Set the main game loop
running = True
while running:
    # Handle user inputs to change the velocity of the snake
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = -0.5
                velocity_y = 0
            if event.key == pygame.K_RIGHT:
                velocity_x = 0.5
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -0.5
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 0.5
                velocity_x = 0

    # Move the snake by adding the current velocity to the head
    snake.insert(0, (snake[0][0] + velocity_x, snake[0][1] + velocity_y))

    # Check if snake goes out of screen
    if snake[0][0] < 0 or snake[0][0] > 790 or snake[0][1] < 0 or snake[0][1] > 590:
        running = False
        print("Game over!")

    # Check for collision with food
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        food = (random.randint(0, 800), random.randint(0, 600))
        snake.append((0, 0))
        score += 1
        print("Score: ", score)
    else:
        snake.pop()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(screen, food_color, (food[0], food[1], food_size, food_size))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
