'''
Q. WAP to print following pattern.

for input n = 5

    * 
   ***
  *****
   ***
    *

n = 5
i = 1,  space = 4 = n - i, star = 1 = 2 * i -1
i = 2,  space = 3 = n - i, star = 3 = 2 * i -1
i = 3,  space = 2 = n - i, star = 5 = 2 * i -1
i = 4,  space = 1 = n - i, star = 7 = 2 * i -1
i = 5,  space = 0 = n - i, star = 9 = 2 * i -1
'''


#n = int(input("Enter a number: "))
n = 5

mid = int((n+1)/2)

for i in range(1, mid+1):
	print("." * (n - i), end="")
	print("*" * (2 * i - 1))

for i in range(n-mid, 0, -1):
    print("." * (n - i), end="")
    print("*" * (2 * i - 1))



