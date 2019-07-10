#Exercise2
#goal create a prime xber generator that uses
#yeild method called run()
#franco pettigrosso

'''
    basic python nothing really much to say
    __INIT__ creates the object
    __iter__ resets the enumeration
    __next__ goes to the next prime number
    is_prime is tell us if the input is a prime
    run goes through the whole list
'''
class prime_numbers:
    def __init__(self, start, end):
        self.a0 = start
        self.b = end

    def __iter__(self):
        self.a = self.a0
        return self

    def __next__(self):
        while(True):
            if self.a < self.b:
                x = self.a
                self.a += 1
                is_prime_number = self.is_prime(x)
                if is_prime_number is False:
                    continue
                return x
            else:
                raise StopIteration
    
    def is_prime(self, x):
        if( x > 1):
            for i in range(2,x):
                if (x % i) == 0:
                    return False
                else:
                    continue
            return True
        return False
    
    def run(self):
        self.a = self.a0
        while(True):
            if self.a < self.b:
                x = self.a
                self.a += 1
                is_prime_number = self.is_prime(x)
                if is_prime_number is False:
                    continue
                yield x
            else:
                raise StopIteration
            
primes = prime_numbers(1,10)
for i in primes.run():
    print(i)