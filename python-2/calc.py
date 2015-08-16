#/usr/bin/python

import calcOps as Ops
import sys
import Tkinter

#if len(sys.argv) < 3 and type(sys.argv[1]) is not int and type(sys.argv[2]) is not int:
#	print "Must provide operator and two operands."
#else:
#	if (type(sys.argv[2]) is int) and (type(sys.argv[3]) is int):
#		print "Addition: ",  Ops.plus(1, 1)
#		print "Subtraction: ", Ops.minus(1, 1)
#		print "Multiplication: ", Ops.cross(1,1)
print "argument length: ", len(sys.argv)
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
res = Ops.cross(num1,num2)
print "Multiplication: ", res
res = Ops.plus(num1,num2)
print "Addition: ", res
res = Ops.minus(num1,num2)
print "Subtraction: ", res