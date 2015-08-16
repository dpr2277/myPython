#/usr/bin/python

def plus(num1, num2):
	if type(num1) is str and type(num2) is str:
		return "Invalid number format. Please enter valid numbers."
	else:
		return "Addition: ", (num1 + num2) 
