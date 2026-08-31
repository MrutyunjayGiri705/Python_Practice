numbers = [1, 2, 2, 3, 2, 4, 3]

max_count = 0
answer = 0

for num in numbers:
    count = numbers.count(num)

    if count > max_count:
        max_count = count
        answer = num

print("Most frequent:", answer)
print("Frequency:", max_count)