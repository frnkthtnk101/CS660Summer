'''
InvertedIndexingGoogle.py
reporduce the logic in chapter
eric, park, tod, franco
'''
from mrjob.job import MRJob
from mrjob.step import MRStep
import os #needed to get the name of the file
import re #to get words

WORD_RE = re.compile(r"[a-z|A-Z]+")


class MRMostUsedWord(MRJob):
    '''
    get the name of the file and takes the words
    of each line given and and assigns a record
    and a count
    '''
    def get_files_and_contents(self, _, line):
            book = str(os.environ['mapreduce_map_input_file']).split('/')[-1]
            for word in WORD_RE.findall(line):
                yield [word.lower(), book], 1
    
    '''
    adds the counts together so make things easier
    on the reducer
    '''
    def combine_word_terms(self, term_book, count):
        yield term_book ,sum(count)
    
    '''
    same thing as the combiner
    '''
    def put_counts (self, term_book, count):
        yield term_book[0], [term_book[1], sum(count)]
    
    '''
    gets are the same term and puts
    them in a list after, yields the
    the term and the frequencies per
    file
    '''
    def reducer(self, term, postings):
        P = []
        for post in postings:
            P.append(post)
        yield term, P

    '''
    we want to know the order of the 
    terms by frequency, or the number
    of times they appear, in all the 
    documents. That happens here.
    '''
    def get_frequency(self, term, postings):
        string_builder = ''
        frequency = 0
        records = []
        for r in postings:
            records.append(r)
        for record in records:
            for book, count in record:
                frequency += count
        string_builder += "{0} {1} ".format(frequency,term)
        for record in records:
            for book, count in record:
                string_builder += "{0} {1}".format(book,count)
        yield None, (frequency, string_builder)
            
    '''
    we want to show the results of
    all of our hard work. The information
    gets sorted at runtime.
    '''
    def show_results(self, _, freq_term ):
        for number, letter in sorted(freq_term, reverse = True):
            yield int(number), letter



    def steps(self):
        return [
            MRStep(
                mapper=self.get_files_and_contents,
                combiner=self.combine_word_terms,
                reducer = self.put_counts
            ),
            MRStep(reducer=self.reducer),
            MRStep(reducer=self.get_frequency),
            MRStep(reducer=self.show_results)
        ]

if __name__ == '__main__':
    MRMostUsedWord.run()