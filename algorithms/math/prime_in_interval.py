'''
Question:
Given two numbers a and b as interval range, the task is to find the prime numbers in between this interval.
'''

class PrimeNumber:
    def __init__(self):
        self.primes=[]

    def make(self, upto):
        is_prime = [True]*(upto+1)
        i=2
        while i*i <= upto:
            if is_prime[i]:
                next = i*i
                while next <= upto:
                    is_prime[next]=False
                    next += i
            i += 1
        self.primes = [i  for i in range(2, upto) if is_prime[i]]

    def all(self):
        return self.primes

    def interval(self, low, high):
        assert low <= high, 'Invalid interval'
        try:
            is_prime = [True]*(high-low+1)
            if low<2:
                low=2
            i=0
            while self.primes[i] * self.primes[i] <= high:
                next = (low // self.primes[i]) * self.primes[i]
                if next < low:
                    next += self.primes[i]
                if next is self.primes[i]:
                    next += self.primes[i]
                while next <= high:
                    is_prime[next-low] = False
                    next += self.primes[i]
                i+=1
            return [low+e for e in range(high-low+1) if is_prime[e]]
        except IndexError:
            print('Interval should be in range from 0 to {}, to increase make more primes using make method'.format(self.primes[len(self.primes)-1]**2-1))
            return


if __name__=='__main__':
    prime = PrimeNumber()
    prime.make(1000)
##    print(prime.all())
    print(prime.interval(low=99000, high=100000))
