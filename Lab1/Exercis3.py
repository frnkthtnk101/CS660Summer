'''
Exercise 3
requirements
get a book count the number of words
and get the average lenght of words

https://stackoverflow.com/questions/7409780/reading-entire-file-in-python#7409814
https://www.geeksforgeeks.org/find-average-list-python/
http://techoverflow.in/remove-special-characters-from-a-string-in-python/python/

question 1
well if a char takes 1 byte we can guess by the number of words in the by 
the average number of bytes per words 
~file size = Word count * average word size
'''
from pathlib import Path #used to get the contents of the file
from statistics import mean #used to get teh average word size

def Main():
    #Put your own path here
    filename2 = '/Users/francopettigrosso/ws/CS660Summer/samples/WarANDPeace.txt'
    len_of_words = []
    contents = Path(filename2).read_text().split(' ')
    number_of_words = len(contents)
    #just to get the len of each word
    for i in contents:
        #just getting special chare
        i = i.strip('\r')
        i = i.strip('\n')
        i = i.strip('\t')
        len_of_words.append(len(i))
    average_word = mean(len_of_words)
    print(f'count {number_of_words}')
    print(f'average length {average_word}')
    print(f'guestimate of file size {average_word * number_of_words} bytes')



Main()