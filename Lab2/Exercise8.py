#exercise 8
#let the machine give us the k most word
#franco
from mrjob.job import MRJob
from mrjob.step import MRStep


#pretty much the same thing as exercise 7 but
#we have the k_word to give us the kth top word
class MRWordFrequencyCount(MRJob):

    k_word = 2

    def mapper_extract_words(self, _, line):
        for i in line.split():
            yield i, 1

    
    def combiner_words(self, key, values):
        yield key, sum(values)
    
    def reducer_combine(self, key, values):
        yield None, (sum(values), key)

    def reducer_sort(self, _, counts):
        i = 0 
        for number, letter in sorted(counts, reverse = True):
            if i == self.k_word:
                yield(letter, int(number))
            i += 1

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