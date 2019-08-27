from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[a-z|A-Z]+")
TXT_MESSAGE = "I love school"

class spam_analizer(MRJob):
    def map_training_data(self, _, line):
        message = line.split(',')
        message_length = len(message)
        for i in range(1,message_length):
            for word in WORD_RE.findall(message[i]):
                yield [word.lower(), message[0]], 1

    def combine_word_terms_ham(self, term_type, count):
        yield None, [term_type[0], term_type[1], sum(count)]

    def reducer_make_dictionary(self, _, term_type_count):
        P = [{},{}]
        for term, classification, count in term_type_count:
            if(classification == "ham"):
                P[0][term] = count
            else:
                P[1][term] = count
        yield P, None
    
    #def reducer_do_calculation_ham(self, ham_dictionary, _):
            
        

    def steps(self):
        return [
            #this is the training data
            MRStep(
                mapper = self.map_training_data,
                reducer = self.combine_word_terms_ham
                ),
            #now we need to calculate
            MRStep(
                reducer = self.reducer_make_dictionary
            )
            ]

if __name__ == '__main__':
    spam_analizer.run()