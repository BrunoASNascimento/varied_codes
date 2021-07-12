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


# test = '2 5 6 9 8 7 4 2 5 8 6 6'
# list_a = test.split(' ')
# print([int(i) for i in list_a])
# print(list(map(int, list_a)))
# print(list_a[::-1])


x = [6.0, 1.4, 1.2, 7.1, 4.6, 2.4, 6.8, 3.3, 6.8, 6.3,
     1.2, 8.2, 3.1, 9.9, 3.9, 7.3, 7.3, 2.9, 9.3, 2.3]
y = [3.1, 3.2, 0.3, 2.7, 2.1, 0.0, 0.0, 1.4, 1.4, 3.2,
     0.0, 1.8, 4.7, 0.6, 1.4, 3.2, 0.3, 1.8, 4.0, 3.2]
cdm = 0.0
n = 20
for i in range(n):
    cdm += (
        (x[i]*y[n-1-i])*(i+1)/(8)
    )

print(cdm)
