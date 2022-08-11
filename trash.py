
#print(solution_(1000))
def solution_(i):
    # Determine prime sequence
    primes = getPrimeNumbers()

    return primes[i:i + 5]


def getPrimeNumbers():
    '''Returns the string of prime
    numbers up to 10k+5 positions.'''

    s = ''
    prime = 2
    while len(s) < 10005:

        # Add new prime to s
        s += str(prime)

        # Calculate next prime
        prime += 1
        while not is_prime(prime):
            prime += 1

    return s


def is_prime(n):
    '''Tests if a number is prime. '''
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def solution(i):
    prime_gap_size = 2000  # Largset prime gap size for primes under 1000000 according to wikipedia
    x = Prime_Sieve(i + (5*prime_gap_size))

    #x = x[i:]
    return "".join([str(j) for j in x])[i:i+5]

def Prime_Sieve(n):
    if n <= 2:
        return []
    prime_bool_array = [True for i in range(n+1)]
    prime_bool_array[0] = False
    prime_bool_array[1] = False

    for i in range(2, int(n**0.5)):
        if prime_bool_array[i]:
            for j in range(i**2,n,i):
                prime_bool_array[j] = False
    # return list(filter(lambda x: x, prime_bool_array))
    return [i for i in range(n) if prime_bool_array[i]]

"""print(solution(0))
# 23571
print(solution(3))

print(solution(346))
assert (solution(0)) == "23751"""

#print list(map(lambda x: int(x),list(getPrimeNumbers())))
#print list(map(lambda x: int(x),("".join([str(j) for j in Prime_Sieve(20232)]))))

print (getPrimeNumbers())
print ("".join([str(j) for j in Prime_Sieve(20232)]))
#assert list(map(lambda x: int(x),list(getPrimeNumbers()))) == list(map(lambda x: int(x),("".join([str(j) for j in Prime_Sieve(20232)]))))