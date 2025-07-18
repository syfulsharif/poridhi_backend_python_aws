n = 7895
digits = []

while n > 0:
    last_digit = n % 10
    digits.append(last_digit)
    n = int(n / 10)

print(digits[::-1])  # Reverse the list to get digits in correct order  