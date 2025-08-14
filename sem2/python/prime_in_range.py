class Prime:
    
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.primes=[]
        
    def Generate_primes(self):
        f=False
        for n in range(self.start, self.end+1):
            for i in range(2,n+1):
                f=True
                if n%i==0 and not i/n==1:
                    f=False
                    break
            if f==True:
                self.primes.append(n)
                
    def display_primes(self):
        print(*self.primes)
        
    def sum_of_prime(self):
        print(sum(self.primes))

start=int(input())
end=int(input())

obj = Prime(start,end)

obj.Generate_primes()

obj.display_primes()

obj.sum_of_prime()