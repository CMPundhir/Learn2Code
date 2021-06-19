# Q1. Write a Python function to multiply all the numbers in a list

def multi(n):
	res = 1
	for x in n:
		res *= x
	return res


r = multi([21,233,4,45,56,67,7,78,8,89])
print(r)