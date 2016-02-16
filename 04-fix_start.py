def fix_start(s):
	substring = s[0]
	s=s.replace(s[0],"*")
	s=s.replace(s[0],substring,1)
	return s

if __name__ == '__main__':
    print('fix_start')
    print(fix_start('babble'), 'ba**le')
    print(fix_start('aardvark'), 'a*rdv*rk')
    print(fix_start('google'), 'goo*le')
    print(fix_start('donut'), 'donut')
