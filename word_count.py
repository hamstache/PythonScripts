import sys


def build_dict(filepath):

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

    word_freq = build_dict(filepath)
    for word, freq in sorted(word_freq.items()):
        print(word + ' ' + str(freq))


def print_top(filepath):

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
