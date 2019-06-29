'''
Exercise 3
requirements
get a book count the number of words
and get the average lenght of words

https://stackoverflow.com/questions/7409780/reading-entire-file-in-python#7409814
https://www.geeksforgeeks.org/find-average-list-python/
http://techoverflow.in/remove-special-characters-from-a-string-in-python/python/
'''
from pathlib import Path
from statistics import mean
import re

def Main():
    filename2 = '/Users/francopettigrosso/ws/CS660Summer/samples/WarANDPeace.txt'
    len_of_words = []
    contents = Path(filename2).read_text().split(' ')
    number_of_words = len(contents)
    for i in contents:
        i = i.strip('\r')
        i = i.strip('\n')
        i = i.strip('\t')
        len_of_words.append(len(i))
    print(f'count {number_of_words}')
    print(f'average length {mean(len_of_words)}')



Main()