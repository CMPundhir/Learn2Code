'''
Q. WAP to print following pattern.

for input n = 5

    * 
   **
  ***
 ****
*****

n = 5
i = 1,  s = 4 = n - i
i = 2,  s = 3 = n - i
i = 3,  s = 2 = n - i
i = 4,  s = 1 = n - i
i = 5,  s = 0 = n - i
'''


n = int(input("Enter a number: "))

for i in range(1, n+1):
	print(" " * (n - i), end="")
	print("*" * i)