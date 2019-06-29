'''
Lab1 Exercise 2
question 1
slightly, but in nudges. THere isnt big enought movement to say authors are different.
question 2
I would just use a histogram to compare
questions 3
the below script shows one how to make an histogram. comments will guide you on how to make it
I followed thes guide lines to make the script
https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
'''
import string
import sys
import matplotlib.pyplot as plt
import numpy as np

ALPHABET = string.ascii_lowercase

def get_letter_count( file_path):
    '''
    exactly the same code you gave us for the frequency script
    except it does it in a function
    '''
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
    '''
    to use the data we need to get the values out of the diction that
    comes out from get_letter_count. we do that here
    '''
    temp_list = []
    for i in ALPHABET:
        temp_list.append(dictionary[i])
    return temp_list


def main():
    '''
    the main script
    -gets the files
    -gets the letter count
    -creates the graph
    -and puts the data in the graph
    -compiles and creates the graph
    '''
    filename1 = '/Users/francopettigrosso/ws/CS660Summer/samples/Heartease.txt'
    filename2 = '/Users/francopettigrosso/ws/CS660Summer/samples/WarANDPeace.txt'
    dataset1 = get_letter_count(filename1)
    dataset2 = get_letter_count(filename2)

    #setup
    ind = np.arange(len(string.ascii_lowercase)) #used to show how big our grap is going to be
    width = .35 #how much space we want between each letter

    fig, ax = plt.subplots()
    wap = get_values_out_of_Dictionary(dataset1)
    heart = get_values_out_of_Dictionary(dataset2)
    #here we are just creating the categories and giving them a label
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

# the script starts here
main()