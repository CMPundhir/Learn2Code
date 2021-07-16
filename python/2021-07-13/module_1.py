'''
Q. What is a Module?
Ans. 1. Consider a module to be the same as a code library.
	2. A file containing a set of functions you want to include in your application.
	3. To create a module just save the code you want in a file with the file extension .py:
'''

def checkPrime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True