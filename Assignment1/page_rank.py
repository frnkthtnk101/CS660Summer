'''
page_rank.py
takes in a matrix and computes the page
rank score using the algorithm from chpt 5
Minining massive data sets...
v′ = βMv + (1 − β)e/n
Eric, Park, Tod, Franco
'''

from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np #need the power function
import os #needed to get the name of the file

class page_rank (MRJob):

    '''
    gets the lines and transforms them
    it will emit the following
    for the left matrix: j,(M, i, mij ) 
    for the right matrix:  j,(N, k, njk) 
    '''
    def map_elements(self, _, line):
        row = line.split('|')
        values = row[1].split(' ')
        matrix_name = str(os.environ['mapreduce_map_input_file']).split('/')[-1]
        is_left_matrix = matrix_name == 'left.txt'
        values_len = len(values)
        for i in range(0,values_len):
            if is_left_matrix:
                    yield (i,(matrix_name,int(row[0]),float(values[i])))
            else:
                yield(int(row[0]),(matrix_name,i,float(values[i])))
    
    '''
    for each j, it will column go colum by column
    on the left matrix and times the row supplied to the right
    also, it will scale by beta and power the left side for
    βMv.
    β is .8 in this scenario
    '''
    def reduce_elements(self, index, values):
        list_of_values = list(values)
        list_O_left = [i for i in list_of_values if i[0] == 'left.txt']
        list_O_rights = [i for i in list_of_values if i[0] == 'right.txt']
        beta = .8
        for left in list_O_left:
            for right in list_O_rights:
                result = (np.power(left[2],1) * beta) * right[2] 
                yield((left[1], right[1]), result) 
    
    '''
    just passes the idedntity but converts it to a string
    to make it look nicer
    '''
    def pass_identity(self, index, values):
        index_string = 'v`{0},{1}='.format(index[0]+1,index[1])
        yield(index_string, values)
    
    '''
    finally we combine the results and add (1 − β)e/n
    which is .05 in this scenario
    '''
    def results(self, index, values):
        yield(index, sum(values) + .05)

    def steps(self):
        return [
            MRStep(
                mapper = self.map_elements,
                reducer = self.reduce_elements
            ),
            MRStep(
                mapper = self.pass_identity,
                reducer = self.results
            )
        ]
        

if __name__ == '__main__':
    page_rank.run()