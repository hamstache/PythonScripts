def both_ends(s):
	if len(s)<2:
		return ""
	return s[0]+s[1]+s[-2]+s[-1]

if __name__ == '__main__':
    print('both_ends')
    print(both_ends('spring'), 'spng')
    print(both_ends('Hello'), 'Helo')
    print(both_ends('a'), '')
    print(both_ends('xyz'), 'xyyz')
