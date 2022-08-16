def solution(i):
    prime_gap_size = 6000
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


