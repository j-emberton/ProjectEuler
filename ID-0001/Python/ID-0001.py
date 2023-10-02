import numpy as np
from math import floor

x = 1000
a = 3
b = 5
def find_factors(x, y):
    z = x/y
    remainder = x%z
    if remainder == 0:
        z = int(z)
        z -= 1
    else:
        z = floor(z)
    
    array = np.zeros(z)
    for i in range(z):
        array[i] = (i+1)*y

    return array

array1 = find_factors(x,a)
array2 = find_factors(x,b)

array = np.unique(np.concatenate((array1,array2),0))
total = np.sum(array)
print(total)