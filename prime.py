from time import time
from timeit import timeit

n = 1000000


def is_prime(i):
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            return False
    return True


def run(n=n):
    #out = ''
    for i in range(2, n):
        if is_prime(i):
            print(' ' + str(i), end='')



def time_it(proc):
    t0 = time()
    proc()
    t = time()-t0
    print()
    print('Done {0} in {1} s.'.format(proc.__name__, round(t, 3)))

#time_it(run)
