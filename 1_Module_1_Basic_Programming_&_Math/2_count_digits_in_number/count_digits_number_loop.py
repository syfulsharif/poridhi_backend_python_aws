# This code counts the number of digits in a number using a loop.

n = 7895
count = 0

while n > 0:
    n = int(n / 10)
    count = count + 1

print(count)  # Output the count of digits
