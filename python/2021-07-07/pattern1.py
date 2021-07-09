'''
Q. WAP to print following pattern.

for input n = 5

*
**
***
****
*****

'''


n = int(input("Enter a number: "))

for x in range(1, n+1):
	print("*" * x)