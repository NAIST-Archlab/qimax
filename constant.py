import numpy as np

def P(i, n = 2):
    result = np.zeros((n,n))
    result[i // n, i % n] = 1
    return result

def state0(n):
    state = np.zeros(2**n)
    state[0] = 1
    return state