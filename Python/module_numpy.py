import numpy as np

array_1D = np.random.rand(3) #one-dimension
array_3D = np.random.rand(3, 3) #three-dimension
print(array_1D)
print(array_3D)

#you can divide the whole array and store it in a different value; using list with thisd would result to an error
array_by_3 = np.array([3, 6, 9, 12, 15, 18])
divided_by_3 = array_by_3/3
print(divided_by_3)