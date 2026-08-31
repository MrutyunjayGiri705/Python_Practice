num = input("Enter number: ")

largest = 0

for digit in num:
    if int(digit) > largest:
        largest = int(digit)

print("Largest digit:", largest)