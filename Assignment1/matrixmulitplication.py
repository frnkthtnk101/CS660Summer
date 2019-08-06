from mrjob.job import MRJob
from mrjob.step import MRStep
import os #needed to get the name of the file


class page_rank (MRJob):

    def map_elements(self, _, line):
        row = line.split('|')
        values = row[2].split(' ')
        size = row[0].split('x')
        matrix_name = str(os.environ['mapreduce_map_input_file']).split('/')[-1]
        is_small_matrix = matrix_name == 'fivebyone.txt'
        values_len = len(values)
        for i in range(0,values_len):
            if is_small_matrix:
                for j in range(0,int(size[0])):
                    yield (j+1,(matrix_name,int(row[1]),int(values[i])))
            else:
                yield(int(row[1]),(matrix_name,i,int(values[i])))
        


    def reduce_elements(self, index, values):
        yield(index, list(values))

    def steps(self):
        return [
            MRStep(
                mapper=self.map_elements,
                reducer = self.reduce_elements
            )
        ]

if __name__ == '__main__':
    page_rank.run()