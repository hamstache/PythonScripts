#!/usr/bin/python3

import sys


def build_dict(filepath):
    '''Given a path to a text file, return a dictionary of the word (key)
    and its frequency, or how often it apears. You need store all the words
    in lowercase, so for example, 'The' and 'the' are counted as the same
    word.

    Note: For this exercise, you don't need to worry about punctuation.

    Hint: Use str.split() (no argument) to split on all whitespace.

    Keyword arguments:
    filepath -- the path to a text file

    Returns: dict
    '''
    # +++your code here+++
    word_freq = {}
    with open(filepath) as text_file:
        for line in text_file:
            words = line.lower().split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
                '''
                # above line is same as below
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
                '''
    return word_freq


def print_words(filepath):
    '''Given a path to a text file, print the word and its frequency in the
    following format:
    word1 count1
    word2 count2
    ...

    The list must be printed sorted and in ascending order by word. This
    function is called when we use --count flag in the command line. You
    should reuse the build_dict function.

    Keyword arguments:
    filepath -- the path to a text file

    Returns: None
    '''
    # +++your code here+++
    word_freq = build_dict(filepath)
    for word, freq in sorted(word_freq.items()):
        print(word + ' ' + str(freq))


def print_top(filepath):
    '''Given a path to a text file, print the top 20 most common words in the
    order that the most common word is first, then the next most common, and
    so on. This function is called when we use --topcount flag in the command
    line. You should reuse the build_dict function.

    Keyword arguments:
    filepath -- the path to a text file

    Returns: None
    '''
    # +++your code here+++
    word_freq = build_dict(filepath)
    sorted_dict = sorted(word_freq.items(), key=lambda w: w[-1], reverse=True)
    for word, freq in sorted_dict[:20]:
        print(word + ' ' + str(freq))

# This basic command line argument parsing code is provided and calls the
# print_words() and print_top() functions which you must define.
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count|--topcount} file')
        sys.exit(1)

    OPTION = sys.argv[1]
    FILEPATH = sys.argv[2]
    if OPTION == '--count':
        print_words(FILEPATH)
    elif OPTION == '--topcount':
        print_top(FILEPATH)
    else:
        print('unknown option: ' + OPTION)
        sys.exit(1)
