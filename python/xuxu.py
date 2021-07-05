# import numpy as np
# x = 20.0*1000
# y = 0.2*1000
# z = 24.0*1000

# while (x <= z):
#     print('branch_1')
#     print(np.around(x % 1000, 2) == 0)
#     print(np.around(x % 1, 2)-0.99 == 0)
#     x += y
# print(z)


test = '2 5 6 9 8 7 4 2 5 8 6 6'
list_a = test.split(' ')
print([int(i) for i in list_a])
print(list(map(int, list_a)))
print(list_a[::-1])
