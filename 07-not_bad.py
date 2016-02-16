import re

def not_bad(s):
	s = re.sub(r"not.*bad","good",s)
	return(s)

if __name__ == '__main__':
    print('not_bad')
    print(not_bad('This movie is not so bad'), 'This movie is good')
    print(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    print(not_bad('This tea is not hot'), 'This tea is not hot')
    print(not_bad("It's bad yet not"), "It's bad yet not")
