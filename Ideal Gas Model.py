from vpython import *
import numpy.random as npr
import time

class Particle:
    def __init__(self,pos,r,vel,q):
        self.radius = r
        self.position = vector(pos[0],pos[1],pos[2])
        self.velocity = vector(vel[0],vel[1],vel[2])
        self.object = sphere(pos = self.position, radius = r)
        self.q = q
    def move(self):
        global DT
        self.position += self.velocity*DT
        self.object.pos = self.position

# Boundary size
b = 100
boundary = box(pos=vector(0,0,0),size=vector(2*b,2*b,2*b),opacity=0.1)

# Time step
DT = 0.1

# List of particles
particle_list = []
numParticles = 100

# Particle properties
pRadius = 1.4
vAvg = 10
vMax = 15
q = 10
e0 = 1

# Additional effects
colorCollisions = True
EM = False

# Generate numParticles particles
for i in range(numParticles):
    particle = Particle([npr.uniform(-b/2.0,b/2.0),npr.uniform(-b/2.0,b/2.0),npr.uniform(-b/2.0,b/2.0)],pRadius,[vAvg*(npr.random()*2-1),vAvg*(npr.random()*2-1),vAvg*(npr.random()*2-1)],q)
    particle_list.append(particle)

# Loop
while True:
    rate(100)
    # Check every particle pair for collisions
    for i in range(len(particle_list)):
        if i != len(particle_list)-1:
            for j in range(i+1,len(particle_list)):
                if mag(particle_list[i].position-particle_list[j].position) <= particle_list[i].radius + particle_list[j].radius:
                    particle_list[i].velocity, particle_list[j].velocity = particle_list[j].velocity, particle_list[i].velocity
                    if colorCollisions == True:
                        particle_list[i].object.color = color.red
                        particle_list[j].object.color = color.blue
                if EM == True:
                    EMForce = (DT*particle_list[i].q*particle_list[j].q)/(4*pi*e0*mag(particle_list[i].position-particle_list[j].position))
                    particle_list[i].velocity, particle_list[j].velocity = (particle_list[i].velocity + EMForce*norm(particle_list[i].position-particle_list[j].position)), (particle_list[j].velocity + EMForce*norm(particle_list[j].position-particle_list[i].position))
                
        # Also check each particle for boundary collisions
        particle = particle_list[i]
        if abs(particle.position.x + particle.radius) >= b:
            particle.velocity.x -= 2*particle.velocity.x
        if abs(particle.position.y + particle.radius) >= b:
            particle.velocity.y -= 2*particle.velocity.y
        if abs(particle.position.z + particle.radius) >= b:
            particle.velocity.z -= 2*particle.velocity.z

        if mag(particle.velocity) >= vMax:
            particle.velocity = norm(particle.velocity)*vMax
                                                                      
        # Move each particle
        particle.move()
