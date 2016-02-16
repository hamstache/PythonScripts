def front_x(words):
	x_list = []
	o_list = []
	for number in words:
		if number[0] == 'x':   	
			x_list.append(number)
		else:
			o_list.append(number)
	x_list.sort()
	o_list.sort()
	return x_list + o_list

if __name__ == '__main__':
    print('front_x')
    print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
