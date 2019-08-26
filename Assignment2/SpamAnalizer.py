from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[a-z|A-Z]+")

class spam_analizer(MRJob):
    def map_training_data(self, _, line):
        message = line.split('\t')
        for word in WORD_RE.findall(message[-1]):
            yield [word.lower(), message[1]], 1


    def steps(self):
        return MRStep(mapper = self.map_training_data)

if __name__ == '__main__':
    spam_analizer.run()