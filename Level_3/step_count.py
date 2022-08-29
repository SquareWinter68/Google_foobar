def solution(n):
    ans = 0
    while True:
        if n == 1:
            return ans
        if n % 2:
            temp_ = [divisible_by_two_n_times(n-1), divisible_by_two_n_times(n+1)]
            if temp_.index(max(temp_)) == 0 or n ==3:
                n -= 1
            else:
                n += 1
            ans += 1
        n = n/2
        ans += 1

def divisible_by_two_n_times(n):
    ans = 0
    while True:
        if n% 2:
            break
        n = n/2
        ans += 1
    return ans