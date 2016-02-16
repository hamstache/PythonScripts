#!/usr/bin/python3

import sys
import re


def extract_names(filename):

    with open(filename) as baby_file:
        text = baby_file.read()
        match = re.search(r'Popularity in (\d+)', text)
        if not match:
            sys.exit(1)
        year = match.group()
        names = [year]

        matches = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',
                             text)
        if not matches:
            sys.exit(1)
        for match in matches:
            (rank, boy_name, girl_name) = match
            names.append((boy_name, int(rank)))
            names.append((girl_name, int(rank)))

    return names


def save_summary(filenames):

    for filename in filenames:
        names = extract_names(filename)
        with open(filename + '.summary', 'w') as summary_file:
            summary_file.write(names[0] + '\n')
            nameranks = [nr[0] + ' ' + str(nr[1])
                         for nr in sorted(names[1:])]
            summary_file.write('\n'.join(nameranks))


def print_summary(filenames):

    for filename in filenames:
        nameranks = extract_names(filename)

        # print header
        print('{:*<22}'.format(''))
        print('* POPULARITY IN', nameranks[0], '*')
        print('{:*<22}'.format(''))

        # print name and rank
        for name, rank in sorted(nameranks[1:]):
            print('{:<18}{:>4}'.format(name, rank))


def main():
    '''Provide the main function of baby_file python file and its usage in
    command line.
    '''
    args = sys.argv[1:]

    if not args:
        print('usage: [--save-summary] file [file ...]')
    elif args[0] == '--save-summary':
        save_summary(args[1:])
    else:
        print_summary(args)


if __name__ == '__main__':
    main()
