#use pip to install numpy: pip install numpy
# Import numpy as np. Random package is a sub-package of numpy
import numpy as np
# Set the seed
np.random.seed(123) #note that the seed has to be random, otherwise it will keep producing the same rand number from the same seed

# #dice throw base code
# # Generate and print random float
# print(np.random.rand())
# # Use randint() to simulate a dice roll (values 1-6, 7 specified is not included)
# print(np.random.randint(1,7))
# step = 50 # initialise start step
# if dice <= 2 : #If dice is 1 or 2, you go one step down.
#     step = step - 1
# elif dice >= 3 and dice <= 5 : #if dice is 3, 4 or 5, you go one step up.
#     step = step + 1
# else: #if dice is 6 (other cases), you throw the dice again.
#     step = step + np.random.randint(1,7)

# Initialize random_walk
random_walk = [0]
for x in range(100) :
    step = random_walk[x] # Set step: last element in random_walk. extracts last element in the list random_walk based on iterator x
    dice = np.random.randint(1,7)
    # Determine next step
    if dice <= 2:
        step = max(0,step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    # append next_step to random_walk
    random_walk.append(step)
print (random_walk)
# Print random_walk

import matplotlib.pyplot as plt
plt.plot(random_walk)
plt.show()