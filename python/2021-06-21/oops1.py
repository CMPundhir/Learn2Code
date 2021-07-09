# OOP : Object oriented programing
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.

# OOP concepts:
# 1. Class
# 2. Object
# 3. Methods
# 4. Polymorphism
# 5. Inheritance
# 6. Abstraction
# 7. Encapsulation
# 8. Aggregation

# --------------------------------*******Class and object ******--------------------------------
# What is Class? 
# A Class is like an object constructor, or a "blueprint" for creating objects.
# A blueprint for an object
# It is a logical entity


# What is Object?
# An object is an instance of a class


# Create a Class
# To create a class, use the keyword class:
class MyClass():
	x = 10


# create an object of a class
o = MyClass()  # <- costructor
print(o.x)


# __init__() method/function
# All classes have a function called __init__(), which is always executed when the class is being initiated.


class Animal():
	"""docstring for Animal"""
	def __init__(self, name, food):
		self.name = name
		self.food = food
		

dog = Animal("Tommy", "pedegree")  # <- constructor call __init__ method
print(dog.name)
print(dog.food)



# --------------------------------*******Method******--------------------------------

# What is method?
# A function inside an object/Class is called method.
# A method always has atleast 1 param of current object. For example self in above example in __init__()


class Human():
	def __init__(self, name2, hobbies):  # <- __init__ is a built-in method, we are overriding it here
		self.name = name2
		self.hobbies = hobbies
		self.habitate = "thal vasi"

	def mySelf(self):  # <- mySelf is a method
		print(f"My name is {self.name}. My habits are {self.hobbies}. I am a Human and a {self.habitate}")


h1 = Human("Pranshu", ["Eating", "sleeping", "Gaming"])
h1.mySelf()
# we can also add other param to an object directly
h1.buriAadat = ["Thod-fodd", "Gandgi machana"]  # <- adding another param to h1 object
h1.acchiAadat = ["Hard-work", "Filling water-bottle"]

# we can use a built  __dict__ to get a dictionary containing all available properties in an object
print(h1.__dict__)










