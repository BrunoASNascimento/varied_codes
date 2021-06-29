import numpy as np
x = 20.0*1000
y = 0.2*1000
z = 24.0*1000

while (x <= z):
    print('branch')
    print(np.around(x % 1000, 2) == 0)
    print(np.around(x % 1, 2)-0.99 == 0)
    x += y
print(z)
