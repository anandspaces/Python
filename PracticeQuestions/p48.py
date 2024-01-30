# generate a list of prime numbers up to a specified limit using sieve of eratosthenes
def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2,int(limit**0.5)+1):
        if sieve[i]:
            for j in range(i*i,limit + 1,i):
                sieve[j] = False
    primes = [num for num in range(2,limit + 1) if sieve[num]]
    return primes

limit = int(input("Enter the limit: "))
print(f"prime numbers are: {sieve_of_eratosthenes(limit)}")