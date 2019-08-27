from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import math

WORD_RE = re.compile(r"[a-z|A-Z]+")
TXT_MESSAGE = "PRIVATE! Your 2003 Account Statement for shows 800 un-redeemed S. I. M. points. Call 08719899230 Identifier Code: 41685 Expires 07/11/04"

class spam_analizer(MRJob):
    def map_training_data(self, _, line):
        message = line.split(',')
        message_length = len(message)
        for i in range(1,message_length):
            for word in WORD_RE.findall(message[i]):
                yield [word.lower(), message[0]], 1

    def combine_word_terms(self, term_type, count):
        yield None, [term_type[0], term_type[1], sum(count)]

    def reducer_make_dictionary(self, _, term_type_count):
        P = [{},{}]
        for term, classification, count in term_type_count:
            if(classification == "ham"):
                P[0][term] = count
            else:
                P[1][term] = count
        yield P, None
    
    def reducer_do_calculation(self, dictionaries, _):
        ham_sum = 0
        spam_sum = 0
        ham_probability = 1
        spam_probability = 1
        ham_keys = dictionaries[0].keys()
        spam_keys = dictionaries[1].keys()
        list_text = WORD_RE.findall(TXT_MESSAGE)
        for i in ham_keys:
            ham_sum += dictionaries[0][i]
        for i in spam_keys:
            spam_sum += dictionaries[1][i]
        for i in list_text:
            if i not in spam_keys:
                dictionaries[1][i] = 1
                spam_sum+=1
            if i not in ham_keys:
                dictionaries[0][i] = 1
                ham_sum += 1

        for i in list_text:
            spam_probability += math.log10(dictionaries[1][i] / spam_sum)
            ham_probability += math.log10(dictionaries[0][i] / ham_sum)

        if ham_probability > spam_probability:
            yield 'ham', None
            
        if ham_probability < spam_probability:
            yield 'spam', None
            
        

    def steps(self):
        return [
            #this is the training data
            MRStep(
                mapper = self.map_training_data,
                reducer = self.combine_word_terms
                ),
            #we need to transpose it
            MRStep(
                reducer = self.reducer_make_dictionary
            ),
            #we then need to run it against the formula
            MRStep(
                reducer = self.reducer_do_calculation
            )
            ]

if __name__ == '__main__':
    spam_analizer.run()