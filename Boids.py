from vpython import *
from numpy import random as rand

# The program class
class RunBoids:
    def __init__(self,numBoids=50,boundary=30):
        # How many boids?
        self.numBoids = numBoids

        # In what size space?
        self.boundary = boundary
        self.boundBox = box(pos=vector(0,0,0),size=vector(2*self.boundary,2*boundary,2*boundary),opacity=0.1)

        # Some values for positioning and setting speeds
        self.randP = boundary*0.65 # Initial positions based on this
        self.randV = boundary*0.15 # Initial speeds based on this
        self.maxV = boundary*0.3 # Max speeds based on this

        # How far can each boid see (in different circumstances)?
        self.neighbourRange = boundary/15
        self.visualRange = boundary/6

        # Factors for abiding by boid rules 1, 2 and 3
        self.separationFactor = 1
        self.alignmentFactor = 1
        self.cohesionFactor = 0.1

        # A time step (to be multiplied by velocity to get distance in each step)
        self.DT = 0.05

        # A list of Boid objects, for referral in loops etc.
        self.Boids = []

        # Begin the program by initialising the boids
        self.makeBoids()

        # Loop and move the boids
        while True:
            rate(100)
            self.moveBoids()

    # A function for making numBoids Boid objects and placing them at random positions
    # within the boundary box. They will also have random initial velocities.
    def makeBoids(self):
        randoms = [0,0,0,0,0,0]
        width = 0.5
        for i in range(self.numBoids):
            for j in range(3):
                randoms[2*j]=(self.randP*(rand.random()*2-1))
                randoms[2*j+1]=(self.randV*(rand.random()*2-1))
            pos = [randoms[0],randoms[2],randoms[4]]
            vel = [randoms[1],randoms[3],randoms[5]]
            self.Boids.append(Boid(pos=pos,vel=vel,width=width))
            
    # A function for moving each boid by invoking its built-in update() function
    def moveBoids(self):
        for boid in self.Boids:
            boid.update(self)

# The Boid class
class Boid(RunBoids):
    # Every boid needs a position, a velocity and a width
    def __init__(self,pos,vel,width):
        self.pos = vector(pos[0],pos[1],pos[2])
        self.vel = vector(vel[0],vel[1],vel[2])
        self.axis = norm(self.vel)
        self.width = width
        # The graphical object for each boid is a unit arrow pointing in the direction
        # of its velocity vector.
        self.object = arrow(pos=self.pos,axis=self.axis,shaftwidth=self.width,round=True)

    # Boid rule 1: avoid your neighbours
    def separate(self,super):
        awayFromNeighbours = vector(0,0,0)
        numNeighbours = 0
        for boid in super.Boids:
            if (boid.object != self.object) and (mag(boid.object.pos-self.object.pos) <= super.neighbourRange):
                awayFromNeighbours -= (boid.object.pos-self.object.pos)
                numNeighbours += 1
        if numNeighbours > 0:
            awayFromNeighbours /= numNeighbours
            awayFromNeighbours *= super.separationFactor
        return awayFromNeighbours

    # Boid rule 2: match the flock's velocity
    def align(self,super):
        alignWithFlock = vector(0,0,0)
        numFlock = 0
        for boid in super.Boids:
            if (boid.object != self.object) and (mag(boid.object.pos-self.object.pos) <= super.visualRange):
                alignWithFlock += (boid.vel-self.vel)
                numFlock +=1
        if numFlock > 0:
            alignWithFlock /= numFlock
            alignWithFlock *= super.alignmentFactor
        return alignWithFlock

    # Boid rule 3: follow the flock
    def cohere(self,super):
        cohereWithFlock = vector(0,0,0)
        numFlock = 0
        for boid in super.Boids:
            if (boid.object != self.object) and (mag(boid.object.pos-self.object.pos) <= super.visualRange):
                cohereWithFlock += (boid.object.pos-self.object.pos)
                numFlock += 1
        if numFlock > 0:
            cohereWithFlock /= numFlock
            cohereWithFlock *= super.cohesionFactor
        return cohereWithFlock

    # Move a boid by adding velocity*time to its position
    def move(self,super):
        self.pos += self.vel*super.DT
        if abs(self.pos.x) >= super.boundary:
            self.pos.x *= -1
        if abs(self.pos.y) >= super.boundary:
            self.pos.y *= -1
        if abs(self.pos.z) >= super.boundary:
            self.pos.z *= -1
        self.object.pos = self.pos

    # Update a boid by applying the 3 rules, then moving it accordingly
    def update(self,super):
        self.vel += self.separate(super) + self.align(super) + self.cohere(super)
        self.axis = norm(self.vel)
        if mag(self.vel) >= super.maxV:
            self.vel = self.axis*super.maxV
        self.object.axis = self.axis
        self.move(super)

# When this script runs, make an instance of the RunBoids class... to run some boids.
if __name__ == "__main__":
    run = RunBoids(30,20)
