def match_ends(words):
	count = 0
	for number in words:
		if len(number) >=2:
			if number[0] == number[len(number)-1]:
				count = count+1
	return count 
 
if __name__ == '__main__':
    print('match_ends')
    print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    print (match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    print(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
