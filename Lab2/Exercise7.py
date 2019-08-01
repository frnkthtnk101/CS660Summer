#exercise 7
#sort the words
from mrjob.job import MRJob
from mrjob.step import MRStep
#https://stackoverflow.com/questions/53707962/mrjob-sort-reducer-output



class MRWordFrequencyCount(MRJob):

    #need to get the words
    def mapper_extract_words(self, _, line):
        for i in line.split():
            yield i, 1

    #combine the words and sum the values
    def combiner_words(self, key, values):
        yield key, sum(values)
    
    #make it in some dict so we can sort
    def reducer_combine(self, key, values):
        yield None, (sum(values), key)

    #sort a yield
    def reducer_sort(self, _, counts):
        for number, letter in sorted(counts, reverse = False):
            yield( letter, int(number))

    #defines the steps in this job
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_extract_words,
                combiner=self.combiner_words,
                reducer=self.reducer_combine
            ),
            MRStep(
                reducer=self.reducer_sort
            )
        ]

if __name__ == '__main__':
    MRWordFrequencyCount.run()
