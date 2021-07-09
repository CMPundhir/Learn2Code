'''
Different forms of Inheritance: 
	1. Single inheritance: 
		When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.

	2. Multiple inheritance: 
		When a child class inherits from multiple parent classes, it is called multiple inheritance. 


Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as a comma-separated list in the bracket. 
'''

class A:
	def justChill(self):
		print("just chill bro...")


class B:
	def gopal(self):
		print("ungli nhi dikhani...")


class C(A, B):
	def __init__(self):
		print("I am inheriting Properties and methods of Class A and B.")


x = C()
x.justChill()
x.gopal()