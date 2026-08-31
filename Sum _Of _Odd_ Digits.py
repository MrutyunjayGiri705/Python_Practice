num = input("Enter number: ")

sum = 0

for digit in num:
    if int(digit) % 2 != 0:
        sum += int(digit)

print("Sum:", sum)