def sort_last(tuples):
	from operator import itemgetter
	tuples.sort(key=itemgetter(1))
	return tuples


if __name__ == '__main__':
    print('sort_last')
    print(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    print(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
