def solution(n,b):
    list_ = []
    ans = 0
    for i in range(100):
        k = len(list(str(n)))
        x = int("".join(sorted(list(str(n)), reverse=True)))
        y = int("".join(sorted(list(str(n)))))
        z = convert_from_decimal(Convert_to_decimal(x, b) - Convert_to_decimal(y, b), b)
        if len(str(z)) < k:
            z = list(str(z))
            for i in range(k - len(z)):
                z = ["0"] + z
            z = "".join(z)
        list_.append(z)
        n = z
    return Counter(list_)

def Convert_to_decimal(numbers_, b):
    numbers_ = map(lambda x: int(x), list(str(numbers_)))
    ans = 0
    if b == 10:
        return int("".join([str(number) for number in numbers_]))
    numbers_.reverse()
    for power,digit in enumerate(numbers_):
        ans += (b**power)* digit
    return ans

def convert_from_decimal(number,to_b):
    remainders = []
    while True:
        if number//2 ==0:
            remainders.append(number % to_b)
            break
        remainders.append(number%to_b)
        number = number//to_b
    return int("".join([str(_) for _ in list(reversed(remainders))]))

def Counter(list_):
    ans = 0
    counter_ = {}
    for i in list_:
        if i in counter_:
            counter_[i] += 1
        else:
            counter_[i] = 1
    for i in counter_:
        if counter_[i] > 1:
            ans +=1

    return ans

