'''
Q. What is Prime Number?
Ans. A number which is divisible by 1 or itself is called prime.
     For example: 2, 5, 7, 11
'''

def isPrime(n):
	if n<2:
		return False
	else:
		for i in range(2, n):
			if n%i==0:
				return False
	return True
