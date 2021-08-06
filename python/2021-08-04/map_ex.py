'''
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
'''


nums = [1,3,5,7]
res = map(lambda n: n*n, nums)
print(res)

for x in res:
	print(x)