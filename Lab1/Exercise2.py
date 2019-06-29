import string
import sys

def get_word_count( file_path):
    infile = open(file_path,'r')
    freq = {}
    count = 0
    for c in string.ascii_lowercase:
        freq[c] = 0

    for line in infile:
        for c in line.lower():
            if c.isalpha():
                freq[c] = freq[c] + 1
                count += 1

    return freq

def main():
    filename1 = 'C:\\Users\\Franco\\ws\\CS660Summer\\samples\\book867.txt'
    filename2 = 'C:\\Users\\Franco\\ws\\CS660Summer\\samples\\WarANDPeace.txt'
    dataset1 = get_word_count(filename1)
    dataset2 = get_word_count(filename2)