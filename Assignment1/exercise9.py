import numpy.matlib
import matlab
import numpy as np 

### with backlinks on page 3
A = np.array([
    [1,1/2,1,0],
    [1/3,0,0,1/2],
    [1/3,0,0,1/2],
    [1/3,1/2,0,0]
    ])
C= np.array([
    [1/4,1/4,1/4,1/4],
    [1/4,1/4,1/4,1/4],
    [1/4,1/4,1/4,1/4],
    [1/4,1/4,1/4,1/4]
])


print(matlab.eig(np.multiply(A,.85)+(np.multiply(C,.15))))

###without backlinks on page 3

A = np.array([
    [0,1/2,1,0],
    [1/2,0,0,1],
    [0,0,0,0],
    [1/2,1/2,0,0]
    ])
C= np.array([
    [1/4,1/4,1/4,1/4],
    [1/4,1/4,1/4,1/4],
    [1/4,1/4,1/4,1/4],
    [1/4,1/4,1/4,1/4]
])


print(matlab.eig(np.multiply(A,.85)+(np.multiply(C,.15))))