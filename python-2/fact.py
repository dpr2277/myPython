#Program integer Factorial
#should pass one integer as an argument

#!/usr/bin/python

import sys

def fact(n):
	f = n
	ret_msg = " "
	if (type(n) is int) and (n > 1): 
		while n > 1:
			f = f * (n - 1)
			n -= 1
		ret_msg = "Factorial for the number is: "
		return f, ret_msg
	else:
		ret_msg = "Please enter positive integer. Try again. Dont enter: "
		return n, ret_msg

if len(sys.argv) > 1:
	try:
		num = int(sys.argv[1])
	except:
		print "Oops!! provided argument is not positive integer. Try again with a number > 0"
	else:
		a, msg = fact(num)
		print msg, a 
else:
	print "Oops!! no argument provided to perform operation \"Factorial\". Try again with a number."
