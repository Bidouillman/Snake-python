import pygame
import random
import time

# Initialize Pygame
pygame.init()
width, height = 400, 400

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 139)
GREEN = (0, 128, 0)
# Set the border size
border_size = 10

# Set the border color
border_color = BLUE

# Initialize the snake
snake = [(200, 200)]
snake_direction = (0, -1)

# Snake speed
speed = 10

# Create the game window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


def draw_border():
    # Fill the screen with the background color (black)
    window.fill(BLACK)

    # Draw the border around the window
    pygame.draw.rect(window, border_color, (0, 0, width, border_size))
    pygame.draw.rect(window, border_color, (0, height - border_size, width, border_size))
    pygame.draw.rect(window, border_color, (0, 0, border_size, height))
    pygame.draw.rect(window, border_color, (width - border_size, 0, border_size, height))


def border_collision(position):
    return (
        position[0] < border_size or
        position[0] >= width - border_size or
        position[1] < border_size or
        position[1] >= height - border_size
    )


# Function to generate a new food position on a 10x10 pixel grid
def new_food(snake):
    while True:
        food = (random.randint(10, width - 20) // 10 * 10, random.randint(10, height - 20) // 10 * 10)
        if food not in snake:
            return food


food = new_food(snake)


# Function to check collision between two elements based on their position
def collision(a, b):
    return a == b


def snake_body_collision(snake):
    for segment in snake[1:]:  # Start from the second segment to avoid checking the head against itself
        if snake[0] == segment:
            return True
    return False


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], 10, 10))


# Update the display
pygame.display.update()

# Wait until the user closes the window
waiting = True
while waiting:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_direction = (-1, 0)
    if keys[pygame.K_RIGHT]:
        snake_direction = (1, 0)
    if keys[pygame.K_UP]:
        snake_direction = (0, -1)
    if keys[pygame.K_DOWN]:
        snake_direction = (0, 1)

    new_head = (snake[0][0] + snake_direction[0] * speed, snake[0][1] + snake_direction[1] * speed)
    snake.insert(0, new_head)  # Add the new head

    # Check if the snake's head has reached the food
    if collision(snake[0], food):
        food = new_food(snake)  # Place new food
    else:
        snake.pop()  # Remove the last segment to simulate movement

    if border_collision(snake[0]) or snake_body_collision(snake):
        waiting = False
    # Call the function to draw the border
    draw_border()
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(food[0], food[1], 10, 10))

    draw_snake(snake)
    pygame.display.flip()
    

print("Game over")
time.sleep(1)
# Quit Pygame
pygame.quit()
