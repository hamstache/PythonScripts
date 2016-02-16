def verbing(s):
	if len(s) < 3:
		return s
	if s[-3]+s[-2]+s[-1] == "ing":
		return s+"ly"
	return s+"ing"

if __name__ == '__main__':
    print('verbing')
    print(verbing('hail'), 'hailing')
    print(verbing('swiming'), 'swimingly')
    print(verbing('do'), 'do')
