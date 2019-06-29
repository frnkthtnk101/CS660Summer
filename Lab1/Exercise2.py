import string
import sys
import matplotlib.pyplot as plt
import numpy as np

ALPHABET = string.ascii_lowercase

def get_word_count( file_path):
    print(f'Starting {file_path}')
    infile = open(file_path,'r')
    freq = {}
    count = 0
    for c in ALPHABET:
        freq[c] = 0

    for line in infile:
        for c in line.lower():
            if c.isalpha():
                try:
                    freq[c] = freq[c] + 1
                    count += 1
                    #just so happens I pick a book with funny letters
                except KeyError: 
                    continue

    for i in ALPHABET:
        freq[i] = freq[i] / count
    return freq

def get_values_out_of_Dictionary ( dictionary):
    temp_list = []
    for i in ALPHABET:
        temp_list.append(dictionary[i])
    return temp_list


def main():
    filename1 = '/Users/francopettigrosso/ws/CS660Summer/samples/Heartease.txt'
    filename2 = '/Users/francopettigrosso/ws/CS660Summer/samples/WarANDPeace.txt'
    dataset1 = get_word_count(filename1)
    dataset2 = get_word_count(filename2)
    print(dataset1)
    print(dataset2)

    #setup
    ind = np.arange(len(string.ascii_lowercase))
    width = .35

    fig, ax = plt.subplots()
    wap = get_values_out_of_Dictionary(dataset1)
    heart = get_values_out_of_Dictionary(dataset2)

    rects1 = ax.bar(ind - width/2, wap, width ,label = "War and peace by Leo Tolstoy")
    rects2 = ax.bar(ind + width/2, heart, width, label='Hearts Charlotte M. Yonge')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('count')
    ax.set_title('letter count by author')
    ax.set_xticks(ind)
    ax.set_xticklabels(ALPHABET)
    ax.legend()
    fig.tight_layout()
    plt.show()


main()