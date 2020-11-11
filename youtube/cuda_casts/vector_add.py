import numpy as np
import time

from numba import vectorize, cuda

@vectorize(['float32(float32, float32)'], target='cuda')
def vector_add(a,b):
    return a+b

def main():
    n = 32000000
    a = np.ones(n, dtype=np.float32)
    b = np.ones(n, dtype=np.float32)

    start = time.time()
    c = vector_add(a, b)
    vector_add_time = time.time() - start

    print("c[:5] = "+ str(c[:5]))
    print("c[-5:] = "+ str(c[-5:]))

    print("vectoradd took for {} seconds".format(vector_add_time))

if __name__ == '__main__':
    main()