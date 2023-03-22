import pygame
import random

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the font
font = pygame.font.SysFont(None, 30)

def draw_array(arr, highlighted_index=None):
    """
    Draws the array and highlights the element at the given index (if any).
    """
    # Clear the screen
    screen.fill(WHITE)
    
    # Set the bar dimensions and spacing
    bar_width = SCREEN_WIDTH // len(arr)
    bar_spacing = 2
    
    # Draw each bar
    for i in range(len(arr)):
        bar_height = arr[i] * (SCREEN_HEIGHT - 50) // max(arr)
        bar_x = i * bar_width + bar_spacing
        bar_y = SCREEN_HEIGHT - bar_height - 50
        bar_color = RED if i == highlighted_index else BLACK
        pygame.draw.rect(screen, bar_color, (bar_x, bar_y, bar_width - bar_spacing, bar_height))
    
    # Draw the index labels
    for i in range(len(arr)):
        label = font.render(str(i), True, BLACK)
        label_x = i * bar_width + bar_width // 2 - label.get_width() // 2
        label_y = SCREEN_HEIGHT - 30
        screen.blit(label, (label_x, label_y))
    
    # Update the display
    pygame.display.update()

def selection_sort(arr):
    """
    Sorts an array in ascending order using selection sort.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Update the visualization
        draw_array(arr, i)
        pygame.time.delay(100)
        
    return arr

# Generate a random array to sort
arr = [random.randint(1, 50) for _ in range(10)]

# Display the initial array
draw_array(arr)

# Sort the array
sorted_arr = selection_sort(arr)

# Display the sorted array
draw_array(sorted_arr)

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()