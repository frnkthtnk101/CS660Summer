#1st algorithm in chapter 5
# x = M v
import numpy.matlib 
import numpy as np 

#this works up to the third step... IDK why

def main():
    A = np.array([
        [0,1/2,1,0],
        [1/3,0,0,1/2],
        [1/3,0,0,1/2],
        [1/3,1/2,0,0]
        ])
    B = np.array([[1/4],[1/4],[1/4],[1/4]])

    steps = np.matmul(np.power(A,2),B)
    print(steps)


main()