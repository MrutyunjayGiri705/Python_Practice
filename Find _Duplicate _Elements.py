numbers = [1, 2, 3, 2, 4, 3, 5]

for num in set(numbers):
    if numbers.count(num) > 1:
        print(num)