def prime_n(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True


def prime_nums(n):
	primes= []
	for i in range(2,n+1):
		if prime_n(i) ==True:
			primes.append(i)
	return primes
	

def get_primefactors(n):
	primelist = prime_nums(n)
	for i in primelist:
		for j in primelist:
			if i * j == n:
				return [i,j]
	
print(get_primefactors(35))