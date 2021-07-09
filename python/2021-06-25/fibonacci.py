'''
fibonacci series
The Fibonacci sequence is one of the most famous formulas in mathematics. Each number in the sequence is the sum of the two numbers that precede it. 

For example: 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 
'''


# all numbers below 100
a = 0
b = 1
while a<100:
	print(a, end=", ")
	a, b = b, a+b

print("\n-----------********------------")


# first 100 number of sequence
a = 0
b = 1
for i in range(25):
	print(a, end=", ")
	a, b = b, a+b


