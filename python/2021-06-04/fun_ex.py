# function
# a function is a block of code
# 1. it only runs when it is called/ invoked
# 2. a function may or may not return a result
# 3. a funciton can take data known as arguments

def sayHi():
	print("Hi")


sayHi()


# types of functions
# 1. function without argument and without return statement
# 2. funciton with argument but without return statement
# 3. function with argument and with return statement
# 	a. function witout default argument
#	b. function with default argument
#		i.  function with posisitonal arguments
#		ii. funciton with named arguments
#		iii.function with varibale arguments
#		iv. funtion with keyword arguments
#		v.  function with both posistional, named, variable and keyword arguments


# a function
def sayHello():
	print("Hello ji")


sayHello()


# funciton with argument
def sayHello(name):
	print("Hello", name)


sayHello("Arushi")


# funciton with default argument
def sayHello(name = "Me"):
	print("Hello", name)


sayHello()
sayHello("CM")


# function with return statement
def calculateInterest(p, t, r = 10):
	return p * r * t / 100


r = calculateInterest(100, 2)
print(r)

r = calculateInterest(100, 2, 12)
print(r)

r = calculateInterest(r = 8, p = 100, t = 2)
print(r)

# varibale argument
def inviteFriends(*frnd):
	for f in frnd:
		print(f, "invited")


inviteFriends("Arushi", "CM", "Koi bhi", "aese hi")



# keyword argument
def myLife(**problems):
	p1 = problems["p1"]
	p2 = problems["p2"]
	if p1 == "kuch_smjh_nhi_aata":
		print("Guidelines to {}:".format(p1), "yoga se hoga...")
	if p2 == "padayi_me_mann_nhi_lagta":
		print(f"Guidelines to {p2}:", "dhyan lagaoo beta... ye bhi yoga se hoga...")


myLife(p1 = "kuch_smjh_nhi_aata", p2 = "padayi_me_mann_nhi_lagta")


# multiple different types of arguments
def mySelf(fname, lname, *friends, **basic_details):

	frnd_str = ""
	for f in friends:
		if frnd_str == "":
			frnd_str = f
		else:
			frnd_str = frnd_str+", "+f 
	my_self = f"I am {fname} {lname}. Hamare mitra gann {frnd_str} bahot nalayak hai.\nHamare pass {basic_details['car']} hai.\nBank balance bs poochoo mt ..."
	return my_self


print(mySelf("Arushi", "Vohra", "x", "y", "z", car = "Camry"))
