numbers = [1, 2, 3, 4, 5, 6]

sum = 0

for num in numbers:
    if num % 2 != 0:
        sum += num

print("Sum:", sum)