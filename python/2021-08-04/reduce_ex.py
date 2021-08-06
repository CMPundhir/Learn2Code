import functools


def adder(x, y):
	#print("x: ",x, ", y: ",y)
	return x+y

nums = [1,3,5,7]
res = functools.reduce(adder, nums)

print(res)


