#exercise 6 find letter frequency by mrjob
#franco
from mrjob.job import MRJob

class word_frequency(MRJob):
    def mapper(self, _, line):
        for c in line.lower():
                try:
                    yield c, 1
                except KeyError: 
                    continue
    
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    word_frequency.run()

