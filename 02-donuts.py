

def donuts(count):
	if count >=10:
		return "Number of donuts: many"
	return "Number of donuts: "+str(count)


if __name__ == '__main__':
    print('donuts')
    print(donuts(4), 'Number of donuts: 4')
    print(donuts(9), 'Number of donuts: 9')
    print(donuts(10), 'Number of donuts: many')
    print(donuts(99), 'Number of donuts: many')
