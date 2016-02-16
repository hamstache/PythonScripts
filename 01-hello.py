
def hello():
	name = input("Please enter your name: ") 
	if len(name)<1:
		print("Hello World")
	else:
		print("Hello "+name)


def main():
	hello()  
