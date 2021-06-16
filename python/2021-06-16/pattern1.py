# WAP to print below pattern for an integer n
"""
Test case 1:
n = 3

*
**
***

Test case 2:
n = 5

*
**
***
****
*****

"""

n = int(input("Enter a number: "))

for i in range(1, n+1):
	print("*" * i)

print("------------------")

for i in range(1, n+1):
	for j in range(1, i+1):
		print("*", end="")
	print()





