import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import math 

'''
1.- Choose a valie and set  the variable x to that value
2.- What is command to compute the square and cube of x
3.- Choose and angle and set the variable theta to its value
4.- What is sin0 cos0? Angles can be measured in degrees or radians
Which of these are being used?
5- Use the np.linspace function to create a row vector called meshPoints
containing exactly 500 values with values evenly spaced between -1 and 1
6.- What expression will yield the value  of the 53th element of meshPoints?
What is this value?
7.- Produce a plot of a sinusoid on the interval [-1,1] using the command
plt.plot(meshPoints,np.sin(2*pi*meshPoints))
'''

x = math.pi/6
print("The square of {} is {}".format(x,x**2))
print("The square of {} is {}".format(x,x**3))

print(math.sin(x))
print(math.cos(x))

