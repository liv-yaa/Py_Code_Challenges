# Ctci Logic & Puzzles (ch 6, p117)
import math
import unittest

class PrimeGen:
	def sieve_of_e(self, max_num):
		""" Generating a List of Primes: The Sieve of Eratosthenes
			* All nonprime nums are divisible by a prime number *
			
			Alg:
				- Start w/ list of all numbers up to max
				- Cross off alt numbers divisible by 2, by 3, ...
				- This gives us a list of all primes
		
		# >>> pg = PrimeGen()
		# >>> pg.sieve_of_e(13)
		


		"""	
		flags = [0, 1] + [True] * (max_num + 1)
		count = 0
		prime = 2

		while prime <= math.sqrt(max_num):
			# Cross off remaining multiples of prime, starting with prime * prime
			for i in range(prime * prime, len(flags), prime):
				flags[i] = False

			break

		return flags



	

	def isPrime(self, n):
		""" Return bool for primality of `n`
			>>> pg = PrimeGen()
			>>> pg.isPrime(13)
			True
			>>> pg.isPrime(2)
			True
			>>> pg.isPrime(14)
			False
		"""
		if n <= 1:
			return False
		
		for x in range(2, n):
			if n % x == 0:
				return False
		return True

		


	def getNextPrime(self, p):
		""" Return the smallest prime number greater than prime `p`  
			>>> pg = PrimeGen()
			>>> pg.getNextPrime(0)
			2
			>>> pg.getNextPrime(2)
			3
			>>> pg.getNextPrime(6)
			7
			>>> pg.getNextPrime(16)
			17
		"""
		if p <= 1:
			return 2

		prime = p
		found = False

		# Loop continuously until isPrime returns True 
		while True:
			prime += 1

			if self.isPrime(prime):
				return prime

		return prime


""" 6.1 Pill Bottle """

def pill_bottle(bottles):
	# Determine which pill bottle contains heavy pills.
	pills = []
	for i, bottle in enumerate(bottles):
		pills += [bottle.pill()] * i

	print(pills)

	weight = sum(pills) # Use the scale one time
	index = (weight - 190) * 10
	return int(index + 0.1)
class Bottle():
	def __init__(self, pill_weight=1.0):
		self.pill_weight = pill_weight

	def pill(self):
		return self.pill_weight



class Test(unittest.TestCase):
  def test_pill_bottle(self):
    bottles = [Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
               Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
               Bottle(), Bottle(), Bottle(), Bottle(), Bottle(1.1),
               Bottle(), Bottle(), Bottle(), Bottle(), Bottle()]
    self.assertEqual(pill_bottle(bottles), 14)
# if __name__ == "__main__":
# 	unittest.main()




""" 6.2 Basketball """












