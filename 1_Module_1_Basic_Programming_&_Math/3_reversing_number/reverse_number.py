def reverse_number(n):
    is_negative = n < 0
    n = abs(n)
    reversed_number = 0

    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10

    if is_negative:
        reversed_number = -reversed_number

    return reversed_number

# Test cases
print(reverse_number(12345))   # Output: 54321
print(reverse_number(-9876))   # Output: -6789
print(reverse_number(0))       # Output: 0

# abs(n) makes the number positive, so we can process it digit by digit.

# % 10 gets the last digit.

# // 10 removes the last digit.

# We multiply reversed_number by 10 and add the digit to build the reversed number.

# If the original number was negative, we just apply the minus sign at the end.

print(reverse_number(508598944))
print(reverse_number(-123456789))
print(reverse_number(1000000))    # Output: 1