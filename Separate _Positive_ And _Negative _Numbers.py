numbers = [10, -5, 8, -2, 7, -9]

positive = []
negative = []

for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive:", positive)
print("Negative:", negative)