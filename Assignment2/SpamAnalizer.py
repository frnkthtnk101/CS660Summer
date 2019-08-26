from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class spam_analizer(MRJob):
    def steps(self):
        return [
            MRStep()
        ]

if __name__ == '__main__':
    spam_analizer.run()