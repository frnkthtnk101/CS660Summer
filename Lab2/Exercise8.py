#exercise 8
#let the machine give us the k most word
#franco
from mrjob.job import MRJob
from mrjob.step import MRStep
#https://stackoverflow.com/questions/53707962/mrjob-sort-reducer-output


class MRWordFrequencyCount(MRJob):

    k_word = 2

    def mapper_extract_words(self, _, line):
        for i in line.split():
            yield i, len(i)

    
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