'''
Create an Iterator

To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
'''


class BhikariIterator:
	def __init__(self, listOfBhikharies):
		self.listOfBhikharies = listOfBhikharies


	def __iter__(self):
		self.id = 0
		return self

	def __next__(self):
		x = self.id
		self.id = x + 1
		if len(self.listOfBhikharies) >= x:
			return self.listOfBhikharies[x]
		else :
			raise StopIteration()


bikhari = BhikariIterator(["CM", "Harshil", "Pranshu"])

itr = iter(bikhari)

print(next(itr))
print(next(itr))
print(next(itr))
#print(next(itr))


