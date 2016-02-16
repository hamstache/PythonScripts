def front_back(a,b):
	a_new = len(a)//2
	b_new = len(b)//2
	if len(a)%2 is not 0:
		a_new = (len(a)+1)//2
	if len(b)%2 is not 0:
		b_new = (len(b)+1)//2
	firsta, seconda = a[:a_new],a[a_new:]
	firstb, secondb = b[:b_new],b[b_new:]
	return firsta+firstb+seconda+secondb

if __name__ == '__main__':
    print('front_back')
    print(front_back('abcd', 'xy'), 'abxcdy')
    print(front_back('abcde', 'xyz'), 'abcxydez')
    print(front_back('Kitten', 'Donut'), 'KitDontenut')
