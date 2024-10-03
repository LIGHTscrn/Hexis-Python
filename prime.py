import math as m

x = int(input("Enter a number: "))

def isprime(x) -> bool:
    if x < 2: 
        return False
    for i in range(2, m.isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

primefactors = []
flag = isprime(x)
if flag:
    print("The number is prime")
else:  
    for i in range(2,m.ceil(x/2)):
        if isprime(i):
            while x%i == 0:
                primefactors.append(i)
                x = x/i
    print(primefactors)
        
