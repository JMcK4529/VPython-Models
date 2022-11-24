from vpython import *
import numpy as np
import time
# In 1D -> a cell has N1 = 2    = -1 + 3**(1)       -> [w,x,y,z]    = [1,1,1,1]     -> living cells need 1 <= n <= 1 to stay alive, dead cells need 1 <= n <= 1 to become alive.
# In 2D -> a cell has N2 = 8    = -1 + 3**(2/1)     -> [w,x,y,z]    = [2,3,3,3]     -> living cells need 2 <= n <= 3 to stay alive, dead cells need 3 <= n <= 3 to become alive.
# In 3D -> a cell has N3 = 26   = -1 + 9**(3/2)     -> [w,x,y,z]    = [2,5,5,5]     -> living cells need 2 <= n <= 5 to stay alive, dead cells need 5 <= n <= 5 to become alive.

# Choose 1D, 2D, 3D
# Choose w,x,y,z


# The overall program class
class GameOfLife:
    # Takes arguments of D = dimension, and
    # w,x,y,z = the limits on the number of neighbours
    # for living cells to stay alive: w <= N <= x
    # and dead cells to become living: y <= N <= z.
    def __init__(self,D,w,x,y,z): 
        self.D = D
        self.params = {"w":w,"x":x,"y":y,"z":z}

        # The size of the game board
        self.size = [15,15,15]

        # A list to contain all of the cells in the game board,
        # for later reference
        self.Cells = []

        # Error checking for dimensionality
        if self.D % 1 == 0 and self.D <= 3 and self.D > 0:
            # Create the game board
            self.initialize(self.D)

            # Loop to play the game
            while True:
                rate(10)
                #time.sleep(1)

                # Move to the next state of the game
                self.next()

        # If the dimensionality is out of bounds, raise a ValueError
        else:
            raise ValueError("The value of D (dimensionality) must be in the range 1 <= D <= 3.")

    # Initialize creates a D-dimensional array of cells and populates it randomly
    def initialize(self,D):
        if D == 1:
            xPoints = np.linspace(-self.size[0]/2, self.size[0]/2, num = self.size[0])
            for point in xPoints:
                aRand = np.random.randint(0,10)
                if aRand == 2:
                    aRand = True
                else:
                    aRand = False
                cell = Cell(vector(point,0,0),aRand)
                self.Cells.append(cell)

        elif D == 2:
            xPoints = np.linspace(-self.size[0]/2, self.size[0]/2, num = self.size[0])
            yPoints = np.linspace(-self.size[1]/2, self.size[1]/2, num = self.size[1])
            for i in range(len(xPoints)):
                for j in range(len(yPoints)):
                    aRand = np.random.randint(0,10)
                    if aRand == 2:
                        aRand = True
                    else:
                        aRand = False
                    cell = Cell(vector(xPoints[i],yPoints[j],0),aRand)
                    self.Cells.append(cell)

        elif D == 3:
            xPoints = np.linspace(-self.size[0]/2, self.size[0]/2, num = self.size[0])
            yPoints = np.linspace(-self.size[1]/2, self.size[1]/2, num = self.size[1])
            zPoints = np.linspace(-self.size[2]/2, self.size[2]/2, num = self.size[2])
            for i in range(len(xPoints)):
                for j in range(len(yPoints)):
                    for k in range(len(zPoints)):
                        aRand = np.random.randint(0,10)
                        if aRand == 2:
                            aRand = True
                        else:
                            aRand = False
                        cell = Cell(vector(xPoints[i],yPoints[j],zPoints[k]),aRand)
                        self.Cells.append(cell)

    # The next() function moves the game to the next state by applying the rules on
    # allowable numbers of neighbours and keeping track of changes to be made...
    # Cell.update() is called afterwards so the new states of cells do not interfere
    # with the rest of the system.
    def next(self):
        for i in range(len(self.Cells)):
            numNeighbours = 0
            for j in range(len(self.Cells)):                                                #change the 1.25 here
                if (i != j) and (mag(self.Cells[j].object.pos-self.Cells[i].object.pos) <= 1.25*np.sqrt(self.D)):
                    if self.Cells[j].status:
                        numNeighbours += 1
            if (self.Cells[i].status) and ((self.params["w"] <= numNeighbours) and (numNeighbours <= self.params["x"])):
                self.Cells[i].survive = True
                #print(i,"Stay") # Debugging
            elif (not(self.Cells[i].status)) and ((self.params["y"] >= numNeighbours) and (numNeighbours >= self.params["z"])):
                self.Cells[i].survive = True
                #print(i,"Live") # Debugging
                
        for cell in self.Cells:
            if cell.survive:
                cell.status = True
                cell.survive = False
            else:
                cell.status = False
            cell.update()

# The Cell class describes any of the individual cells in the game which can be
# either alive (opacity 1) or dead (opacity 0.1).
# The Cell.survive property describes whether the Cell should become alive or dead on
# calling the Cell.update() method.
class Cell:
    def __init__(self, pos, status = False):
        self.status = status
        self.object = box(pos=pos,size=vector(1,1,1))
        self.survive = False
        self.update()

    def update(self):
        if self.status:
            self.object.color = color.red
            self.object.opacity = 1
        else:
            self.object.color = color.gray(0.9)
            self.object.opacity = 0.1
            
        
# When this .py file runs, instantiate a Game.
if __name__ == "__main__":
    #run1D = GameOfLife(1,1,1,1,1)
    run2D = GameOfLife(2,2,3,3,3)
    #run3D = GameOfLife(3,3,5,5,5)
        
