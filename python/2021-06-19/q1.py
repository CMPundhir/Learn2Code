# Q1. Write a Python function to sum all the numbers in a list

def add(list1):
	res = 0
	for x in list1:
		res += x
	return res


r = add([21,233,4,45,56,67,7,78,8,89])
print(r)