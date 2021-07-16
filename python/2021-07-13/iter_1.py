'''
Python Iterators

1. An iterator is an object that contains a countable number of values.
2. An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
3. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of 
   the methods __iter__() and __next__().


Q. Difference between Iterator vs Iterable?
Ans. Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you 
can get an iterator from.
'''


games = ["Minecraft", "COD", "PUBG", "Mini Militia"]
myitr = iter(games)
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))



'''
Even strings are iterable objects, and can return an iterator:

'''

name = "Chander Mohan Pundhir"
itr = iter(name)

c = next(itr)
while c:
	print(c)
	try:
		c = next(itr)
	except StopIteration:
		c = None


'''
The for loop actually creates an iterator object and executes the next() method for each loop.

'''

x = range(10)
res = isinstance(x, range)
print(res)

for x in games:
	print(x)


