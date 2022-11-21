# Sum primes below 2 milions. In this sulution I applied Sieve of Erastones 
def erastones():
    a = [True] * 2000000
    a[0] = a[1] = False
    sum = 0
    for (i, isprime) in enumerate(a):
        if isprime:
            sum += i
            for n in range(i*i, len(a), i):
                a[n] = 0
    
    return sum

print(erastones())

# The output is : 142913828922
