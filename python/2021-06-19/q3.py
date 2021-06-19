# Q3. Write a Python program to reverse a string

# sol with slice operator
def reverseStr(s):
	return s[::-1]


r = reverseStr("Chander Mohan Pundhir")
print(r)

range(0, 10, -2)

# sol with loop
def reverseStr2(s):
	revS = ""
	lastIndex = len(s)-1
	for i in range(lastIndex, -1, -1):
		print(i," : ", s[i])
		revS += s[i]
	return revS;


r = reverseStr2("Chander Mohan Pundhir")
print(r)
