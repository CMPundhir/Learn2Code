'''
The filter() method filters the given sequence with the help of a function 
that tests each element in the sequence to be true or not.
'''

nums = [1,2,3,567,7,78,89,90,8]
res = filter(lambda n: n%2!=0, nums)
print(res)

for x in res:
	print(x)