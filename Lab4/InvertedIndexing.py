from mrjob.job import MRJob
from mrjob.step import MRStep
import os
import re

WORD_RE = re.compile(r"[a-z|A-Z]+")

class MRMostUsedWord(MRJob):
    
    h = {}

    def get_files_and_contents(self, _, file_path):
        file_contents = open(file_path,'r')
        book = str( os.path.basename(file_path))
        for line in file_contents:
            words = WORD_RE.findall(line)
            for word in words:
                yield [word.lower(), book], None
        
    def split_words(self, word, terms):
        the_word = word[0] 
        t = word[1]
        is_a_key =  the_word  in self.h.keys()
        if(is_a_key):
            try:
                self.h[the_word][t] += 1
            except:
                self.h[the_word][t] = 1
            '''
            is_a_term = t in self.h[the_word].keys()
            if(is_a_term):
                self.h[the_word][t] += 1
            else:
                self.h[the_word][t] = 1
            '''
        else:
            self.h[the_word]= {t : 1}
        yield None, None
    
    def reducer (self, _, __):
        for i in self.h.keys():
            yield i, self.h[i]

    def steps(self):
        return [
            MRStep(
                mapper=self.get_files_and_contents,
                reducer=self.split_words
            ),
            MRStep(reducer=self.reducer)
        ]

if __name__ == '__main__':
    MRMostUsedWord.run()