# This code counts the number of digits in a number using logarithmic expression.

import math

n = 7895

# AI suggested code
# def count_digits(n: int) -> int:
#     if n == 0:
#         return 1
#     return int(math.log10(n)) + 1


# Lecture Video Code
def count_digits(n: int) -> int:
    power = int(math.log10(n))
    return power + 1 # 0(1) time complexity

if __name__ == "__main__":
    print(count_digits(n))  # Output the count of digits