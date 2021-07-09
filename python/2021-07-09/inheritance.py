"""
Q. What is Inheritance?
Ans. Inheritance allows us to define a class that inherits all the methods and properties from another class.
	1. Parent class is the class being inherited from, also called base class.
	2. Child class is the class that inherits from another class, also called derived class.


Q. What are the benefits of Inheritance?
Ans. 1. It represents real-world relationships well.
	 2. It provides reusability of a code. We don’t have to write the same code again and again. 
	 	Also, it allows us to add more features to a class without modifying it.
	 3. It is transitive in nature, which means that if class B inherits from another class A, 
	 	then all the subclasses of B would automatically inherit from class A.
"""

class Animal:
	def __init__(self, name, age, food, hebitate):
		self.name = name
		self.age = age
		self. food = food
		self.hebitate = hebitate

	def intro(self):
		print(self.__dict__)


a1 = Animal("Tomy", 10, ["Pedegree", "bread"], "Pet house")
a1.intro()


class TelePhone:
	def __init__(self, generation, medium, brand):
		self.generation = generation
		self.medium = medium
		self.brand = brand

	def makeACall(self):
		print("calling...")


class SmartPhone(TelePhone):
	def __init__(self, generation, medium, brand, camera, processor):
		super().__init__(generation, medium, brand)
		self.camera = camera
		self.processor = processor
		self.brand = brand
		

class BarPhone(TelePhone):
	def __init__(self, generation, medium, brand, is_torch, battery_backup):
		super().__init__(generation, medium, brand)
		self.is_torch = is_torch
		self.battery_backup = battery_backup


s1 = SmartPhone("4G", "wireless", "MI", "12 MP", "SD 880")
b1 = BarPhone("2G", "wireless", "Nokia", True, "20 days")


s1.makeACall()

print(s1.__dict__)
print(b1.__dict__)
