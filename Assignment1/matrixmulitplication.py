from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np
import os #needed to get the name of the file


class page_rank (MRJob):

    def map_elements(self, _, line):
        row = line.split('|')
        values = row[1].split(' ')
        matrix_name = str(os.environ['mapreduce_map_input_file']).split('/')[-1]
        is_small_matrix = matrix_name == 'fivebyfive.txt'
        values_len = len(values)
        for i in range(0,values_len):
            if is_small_matrix:
                    yield (i,(matrix_name,int(row[0]),float(values[i])))
            else:
                yield(int(row[0]),(matrix_name,i,float(values[i])))
        
    def reduce_elements(self, index, values):
        list_of_values = list(values)
        list_O_left = [i for i in list_of_values if i[0] == 'fivebyfive.txt']
        list_O_rights = [i for i in list_of_values if i[0] == 'fivebyone.txt']
        beta = .8
        i_beta = round((1-beta)/4,5)
        for left in list_O_left:
            for right in list_O_rights:
                result = ((np.power(left[2],1) * beta) * right[2]) + i_beta
                yield((left[1], right[1]), result) 
    
    def pass_identity(self, index, values):
        yield(index, values)
    
    def results(self, index, values):
        yield(index, sum(values))

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