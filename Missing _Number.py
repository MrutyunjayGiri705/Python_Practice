numbers = [1, 2, 3, 5, 6]

n = 6

total = n * (n + 1) // 2
sum = 0

for num in numbers:
    sum += num

print("Missing number:", total - sum)