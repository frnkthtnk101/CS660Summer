#1st algorithm in chapter 5
import numpy.matlib 
import numpy as np 


def main():
    A = np.array([
        [0,1/2,1,0],
        [1/3,0,0,1/2],
        [1/3,0,0,1/2],
        [1/3,1/2,0,0]
        ])

    B = np.array([[1/4],[1/4],[1/4],[1/4]])

    C = np.matmul(A,B) 
    

    print(C)


main()