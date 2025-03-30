import numpy as np

def GP(a, r, n):
    r = np.asarray(r) 
    if np.any(r < 1):  
        return a * (1 - r**n) / (1 - r)
    else:
        return a * (r**n - 1) / (r - 1)

print(GP(5, 2, 4))