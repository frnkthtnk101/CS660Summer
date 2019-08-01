#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:11:20 2019

@author: Mac
"""

#inverse index method 1 (non-optimal)

from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import os

WORD_RE = re.compile(r"[\w']+")

class MRMostUsedWord(MRJob):

    def mapper(self, _, filepath):
        file_contents = open(filepath,'r')
        book = str( os.path.basename(filepath))
        for line in file_contents:
            for term in WORD_RE.findall(line.strip()):
                yield [term.lower(), book], 1

    def combiner(self, term_book, termf):
        #counts the number of occurances of a term in each book
        yield (term_book, sum(termf))

    def reducer_primary(self, term_book, count):
        #generates postings
        term = term_book[0]
        book_id = term_book[1]
        yield (term, [book_id, sum(count)])

    
    def reducer_secondary(self, term, posting):
        # this is the part I'm not sure about -- was following logic shown in power
        P = []
        for post in posting:
            P.append(post)
        for post in sorted(P, reverse=True):
            yield term, P

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer_primary),
            MRStep(reducer=self.reducer_secondary)
        ]


if __name__ == '__main__':
    MRMostUsedWord.run()
