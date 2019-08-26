import numpy.matlib
import matlab
import numpy as np 


A = np.array([
    [0,0,1,1/2],
    [1/3,0,0,0],
    [1/3,1/2,0,1/2],
    [1/3,1/2,0,0]
    ])
B= np.array(
    [
        [1],
        [1],
        [1],
        [1]
    ]
)
print(np.core.matmul(A,B))
