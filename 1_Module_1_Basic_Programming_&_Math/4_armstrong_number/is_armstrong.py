def is_armstrong_number(num):
    given_num = num
    sum_of_cubes = 0
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10
    return sum_of_cubes == given_num


# Test cases
print(is_armstrong_number(153))  # Output: True
print(is_armstrong_number(370))  # Output: True
print(is_armstrong_number(371))  # Output: True
print(is_armstrong_number(9474)) # Output: True
print(is_armstrong_number(123))  # Output: False
print(is_armstrong_number(0))    # Output: True
print(is_armstrong_number(1))    # Output: True