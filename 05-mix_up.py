def mix_up(a,b):
	a01=a[0]+a[1]
	b01=b[0]+b[1]
	anew=a.replace(a[0]+a[1], b01)
	bnew=b.replace(b[0]+b[1], a01)
	return anew+" "+bnew	


if __name__ == '__main__':
    print('mix_up')
    print(mix_up('mix', 'pod'), 'pox mid')
    print(mix_up('dog', 'dinner'), 'dig donner')
    print(mix_up('gnash', 'sport'), 'spash gnort')
    print(mix_up('pezzy', 'firm'), 'fizzy perm')
