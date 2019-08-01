from mrjob.job import MRJob
from mrjob.step import MRStep
import os
import re

WORD_RE = re.compile(r"[a-z|A-Z]+")

class MRMostUsedWord(MRJob):
    
    h={}

    def get_files_and_contents(self, _, file_path):
        file_contents = open(file_path,'r')
        book = str( os.path.basename(file_path))
        for line in file_contents:
            words = WORD_RE.findall(line)
            for word in words:
                yield [word.lower(), book], 1
        
    def combine_word_terms(self, selection, count):
        self.h[selection[0]] = []
        yield selection ,sum(count)
    
    def put_counts (self, selection, count):
        self.h[selection[0]].append([selection[1], sum(count)])
        yield None, None
    
    def reducer(self, _, __):
        for i in self.h.keys():
            for j in self.h[i]:
                yield (f"{i} {j[0]}", int(j[1]))

    def steps(self):
        return [
            MRStep(
                mapper=self.get_files_and_contents,
                combiner=self.combine_word_terms,
                reducer = self.put_counts
            ),
            MRStep(reducer=self.reducer)
        ]

if __name__ == '__main__':
    MRMostUsedWord.run()