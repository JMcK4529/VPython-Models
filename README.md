# VPython Models

## Summary
This project includes some examples of VPython code useful for rudimentary physics simulations, as well as other models of interest (e.g. John Conway's Game of Life).

## Boids

### Project Description
Boids are a simple way of modelling the behaviour of murmurations in flocks of birds, or the schooling behaviour of fish.
Each Boid followsa set of rules:
1. Maintain separation from neighbours.
2. Align with the orientation of neighbours.
3. Cohere with the centre of the flock.

### How to Install Boids
1. Ensure you have a Python IDE and have the following libraries installed:
      - VPython
      - Numpy
2. Download "Boids.py".

### How to Use Boids
1. Open Boids.py in your Python IDE.
2. In line 133, choose values for the number of Boids and the side length of their container.
      - RunBoids() will use the default values: 50 Boids and side length of 30.
      - RunBoids(x,y) will produce x Boids in a y side length container.
3. Run the script.

## Ideal Gas Model

### Project Description
"numParticles" particles, modelled as spheres are generated within a cube shaped container. The particles elastically collide with the container and each other.

### How to Install Ideal Gas Model
1. Ensure you have a Python IDE and have the following libraries installed:
      - VPython
      - Numpy
2. Download "Ideal Gas Model.py".

[//]: # (### How to Use Ideal Gas Model 1. 2. )

## Game of Life

### Project Description
This project extends John Conway's Game of Life into 1D and 3D. The rules associated with allowable numbers of neighbours can be adjusted to experiment with different systems.

### How to Install Game of Life
1. Ensure you have a Python IDE and have the following libraries installed:
      - VPython
      - Numpy
2. Download "Game of Life.py".

[//]: # (### How to Use Game of Life 1. 2. )


## Credits
Author: Joseph McKeown  

## Licence

Copyright (C) 2022 Joseph McKeown

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,      
but WITHOUT ANY WARRANTY; without even the implied warranty of       
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        
GNU General Public License for more details.                         
                                                                     
You should have received a copy of the GNU General Public License    
along with this program.  If not, see <http://www.gnu.org/licenses/>.
