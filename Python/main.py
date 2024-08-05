import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the size of the grid
grid_size = 50

# Create the initial grid
grid = np.random.randint(2, size=(grid_size, grid_size))

# Define the rules of the game
def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            # Count the number of living neighbors
            neighbors = count_neighbors(grid, i, j)
            # Apply the rules of the game
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
            else:
                new_grid[i, j] = grid[i, j]
    return new_grid

# Helper function to count the number of living neighbors
def count_neighbors(grid, i, j):
    neighbors = 0
    for x in range(max(0, i - 1), min(grid_size, i + 2)):
        for y in range(max(0, j - 1), min(grid_size, j + 2)):
            if (x, y) != (i, j):
                neighbors += grid[x, y]
    return neighbors

# Create the figure and axes
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='gray')

# Define the animation function
def animate(frame):
    global grid
    grid = update_grid(grid)
    img.set_array(grid)
    return img,

# Run the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=True)

# Show the animatio
plt.show()
