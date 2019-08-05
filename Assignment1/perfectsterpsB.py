#2st algorithm in chapter 5
# v′ = βMv + (1 − β)e/n

import numpy.matlib 
import numpy as np 

#this works up to the third step... IDK why

def main():
    A = np.array([
        [0,1/2,0,0],
        [1/3,0,0,1/2],
        [1/3,0,1,1/2],
        [1/3,1/2,0,0]
        ])
    e = np.array([[1],[1],[1],[1]])
    beta = .8
    i = round((1-beta)/4,5)
    i_beta = np.multiply(e,i)

    B = np.array([[1/4],[1/4],[1/4],[1/4]])

    

    steps = np.add(
        np.matmul(
            np.multiply(
                np.power(A,2),beta),B),i_beta)
    print(steps)


main()