import pygame

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create the two paddles and the ball
paddle1 = pygame.Rect(10, 250, 20, 100)
paddle2 = pygame.Rect(770, 250, 20, 100)
ball = pygame.Rect(390, 290, 20, 20)

# Set a slower initial velocity for the ball
ball_velocity = [1, 1]

# create the score variables
score1 = 0
score2 = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= 5
    if keys[pygame.K_s] and paddle1.y < 500:
        paddle1.y += 5
    if keys[pygame.K_UP] and paddle2.y > 0:
        paddle2.y -= 5
    if keys[pygame.K_DOWN] and paddle2.y < 500:
        paddle2.y += 5

    # Move the ball
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Check for collisions with the paddles and walls
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_velocity[0] = -ball_velocity[0]
    if ball.y <= 0 or ball.y >= 580:
        ball_velocity[1] = -ball_velocity[1]
    if ball.x <= 0:
        score2 += 1
        ball.x, ball.y = 390, 290
    if ball.x >= 780:
        score1 += 1
        ball.x, ball.y = 390, 290

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddles and ball
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    
    # Draw the score
    font = pygame.font.Font(None, 30)
    score_text1 = font.render("Player 1: " + str(score1), 1, (255, 255, 255))
    score_text2 = font.render("Player 2: " + str(score2), 1, (255, 255, 255))
    screen.blit(score_text1, (650, 10))
    screen.blit(score_text2, (100, 10))
    
    # Update the display
    pygame.display.set_caption("Ping Pong - Player 1: " + str(score1) + " Player 2: " + str(score2))
    pygame.display.update()

# Clean up and exit
pygame.quit()

