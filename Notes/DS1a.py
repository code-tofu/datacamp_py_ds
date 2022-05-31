#C3.2 METHODS

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = str.upper(place)

# Print out place and place_up
print(place)
print(place_up)
# Print out the number of o's in place
print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)



#C3.3 PACKAGES
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = math.pi * 2 * r

# Calculate A
A = math.pi * r * r

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Import radians function of math package
from math import radians
phi = radians(12)

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * phi

# Print out dist
print(dist)



#C3.4 NUMPY
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
# print (bmi)
print (light)

# Print out BMIs of all baseball players whose BMI is below 21
print (bmi[light])


# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball [:,1]

# Print out height of 4th player
print(np_baseball[3][0])


np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
# array([[ 2,  4],
#        [ 6,  8],
#        [10, 12]])

np_mat + np.array([10, 10])
# array([[11, 12],
#        [13, 14],
#        [15, 16]])
# adds 10 to all elements

np_mat + np_mat
# array([[ 2,  4],
#        [ 6,  8],
#        [10, 12]])
# note that np_mat does not change


# heights and positions are available as lists
positions = ['GK', 'M', 'A', 'D', 'GK', 'M', 'A', 'D'] #...
heights = [191, 184, 185, 180,191, 184, 185, 180] #...
# Import numpy
import numpy as np
# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)
# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']
# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']
# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))