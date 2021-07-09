from prime import isPrime
import datetime


def checkSingle():
	n = int(input("Enter a number: "))
	str = f"{n} is a Prime." if isPrime(n) else f"{n} not a prime"
	print(str)


def checkRange():
	start = int(input("Enter range starting : "))
	end = int(input("Enter range ending : "))
	primeList = []
	sTime = datetime.datetime.now()
	for x in range(start, end+1):
		if isPrime(x):
			primeList.append(x)
	eTime = datetime.datetime.now()
	tDiff = eTime - sTime
	print(f"Time taken: {tDiff}")
	print(f"Total prime between {start} and {end} : {len(primeList)}")
	return primeList


choice = int(input("Enter your choice: \n1 : Check a Single Prime\n2 : Check Rnage\nEnter Here : "))
if choice == 1:
	checkSingle()
elif choice == 2:
	checkRange()
else:
	print("Invalid choice")


#999,990,000,000
