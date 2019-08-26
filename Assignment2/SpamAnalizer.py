from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[a-z|A-Z]+")

class spam_analizer(MRJob):
    def map_training_data(self, _, line):
        message = line.split(',')
        message_length = len(message)
        for i in range(1,message_length):
            for word in WORD_RE.findall(message[i]):
                yield [word.lower(), message[0]], 1

    def combine_word_terms(self, term_type, count):
        yield term_type ,sum(count)

    def steps(self):
        return MRStep(mapper = self.map_training_data, reducer = self.combine_word_terms)

if __name__ == '__main__':
    spam_analizer.run()