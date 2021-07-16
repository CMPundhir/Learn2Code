'''
Python Scope

A variable is only available from inside the region it is created. This is called scope


Scope types:
	1. local scope
	2. global scope
'''

x = 100 # x has global scope

def testX():
	global y # this will make y global
	print("inside funciton, x = ",x)
	y = 200 # y has local scope if we don't define line 15
	print("inside function, y = ", y)

print("In module, x = ",x)
testX()

# we cannot access y here due to its local scope in testX function. try removing line 15 to test it
print(y) 

