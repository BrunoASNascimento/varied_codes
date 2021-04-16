import time
from numba import njit


@njit(fastmath=True, cache=True)
def sum_pair_numbers(num_Max):
    sum_pair = 0
    control = 0
    while control < num_Max:
        if control % 2 == 0:
            sum_pair += control
        control += 1
    return sum_pair


if __name__ == '__main__':
    start = time.time()
    print(f'Sum: {sum_pair_numbers(10_000_000)}')
    end = time.time()
    print(f'{end-start} s')
