
def checkPrime(n):
	if n==1 : return False
	for i in range(2, n):
		if n%i == 0:
			return False
	return True


nums = list(map( int, input("Enter array: ").split()))
print(nums)

primes = list(filter( checkPrime, nums))
print(primes)