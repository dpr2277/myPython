__author__ = 'Prudhvi'

def fact(n):
    """ this function is to return the factorial of the number passed to it"""
    f = 1
    for i in range(1, n+1):
        f *= i
    print('The value of x in fact : ', x)
    return f

def list_sqr(n):
    li = {}
    for i in range(1, n+1):
        li[i] = i*i
    return li

print('Enter an integer: ')
x = int(input())
print('The factorial of ', x, ' is : ', fact(x))
print('The pair of squares for ', x, ' is : ', list_sqr(x))

try:
    print("a")
    raise Exception("Doom")
except:
    print("b")
else:
    print("c")
finally:
    print("d")