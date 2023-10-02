import numpy as np

x=2
y1 = 1
y2 = 2
z = 2
while z <= 4000000:

    y3 = y1+y2
    if y3%2 == 0:
        z = z + y3
    y1 = y2
    y2 = y3
    x += 1
    print(x)

print(x)
print(z)
