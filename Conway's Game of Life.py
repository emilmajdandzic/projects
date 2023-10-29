import numpy as np
import matplotlib.pyplot as plt

class GameOfLife(object):  
    """
    Constructs an instance of Conway's Game of Life
    
    Attributes:
    x_dim : int
        x dimension of grid
    y_dim : int
        y dimension of grid
    grid: 2-D array
        grid containing all cells and their state
    
    Methods:
    get_grid()
        Prints the 2-D array containing the current state of the grid.
    print_grid()
        Prints the current state of the grid in a human readable way.
    populate_grid(coord)
        Populates the game grid with live cells at the specified coordinates.
    make_step()
        Makes one step in Conway's Game of Life.
    make_n_steps(n)
        Makes n steps in Conway's Game of Life.
    draw_grid()
        Makes a scatter plot displaying the current state of the grid.   
    """
    
    def __init__(self, x_dim, y_dim):
        """
        Initialises the instance of Conway's Game of Life.
        
        Parameters:
        x_dim: int. The dimenison in x of the grid.
        y_dim: int. The dimenison in y of the grid.
        grid: array of zeros. The grid containing all cells and their state.
        """
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.grid = np.zeros((y_dim, x_dim), dtype=int)
    
    def get_grid(self):
        """
        Prints the 2-D array containing the current state of the grid.
        
        Returns:
        The grid.
        """
        return self.grid


    def print_grid(self):
        """
        Prints the current state of the grid in a human readable way.
        
        Returns:
        The grid.
        """
        for y in range(self.y_dim):
            row = ""
            for x in range(self.x_dim):
                row += str(self.grid[y][x])
                row += " | "
            print(row)
            print("-" + (2*x+1) * " -")


    def populate_grid(self, coord):
        '''
        Populates the game grid with live cells at the specified coordinates.

        Parameters:
        coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.

        Returns:
        The updated grid with the new live cells.
        '''
        
        for row, col in coord:
            self.grid[row][col] = 1

    def make_step(self):
        """
        Makes one step in Conway's Game of Life.
        
        Returns:
        The updated grid with the states of the cells after one step in Conway's
        Game of Life.
        """
        updated_grid = np.copy(self.grid)
        for y in range(self.y_dim):
            for x in range(self.x_dim):
                current_cell = self.grid[y][x]
                nbh_x = [x_coord for x_coord in [x-1, x, x+1] \
                         if x_coord >= 0 and x_coord < self.x_dim]
                nbh_y = [y_coord for y_coord in [y-1, y, y+1] \
                         if y_coord >= 0 and y_coord < self.y_dim]
                neighbours = [self.grid[y_coord][x_coord] for y_coord in nbh_y for x_coord in nbh_x \
                              if not (y_coord == y and x_coord == x)]
                
                live_nbh = sum(neighbours)
                if current_cell:
                    if live_nbh == 2 or live_nbh == 3:
                        pass
                    else:
                        updated_grid[y][x] = 0
                else:
                    if live_nbh == 3:
                        updated_grid[y][x] = 1
        self.grid = updated_grid.copy()
        
    def make_n_steps(self, n):
        """
        Makes n steps in Conway's Game of Life.
        
        Parameters:
        n: int. Number of steps to be done in Conway's Game of Life.
        
        Returns:
        The updated grid with the states of the cells after n steps in Conway's
        Game of Life.
        """
        for _ in range(n):
            self.make_step()


    def draw_grid(self):
        """
        Makes a scatter plot displaying the current state of the grid.
        
        Returns:
        The scatter plot showing the grid and live/dead cells in blue/grey respectively.
        """
        x_coord, y_coord, colour = [], [], []
        col_transform = {0: "grey", 1: "blue"}
        for y in range(self.y_dim):
            for x in range(self.x_dim):
                x_coord.append(x)
                y_coord.append(y)
                colour.append(col_transform[self.grid[y][x]])
        y_coord = [-i for i in y_coord]
        plt.scatter(x_coord, y_coord, c=colour, marker="s")
        plt.axis("off")
