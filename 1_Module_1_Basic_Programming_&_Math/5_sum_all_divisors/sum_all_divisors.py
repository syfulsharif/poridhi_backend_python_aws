sum = 0

def sum_all_divisors(n):
    global sum
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
            print(i)
    return sum

print(sum_all_divisors(12))
