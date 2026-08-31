num = input("Enter number: ")

smallest = 9

for digit in num:
    if int(digit) < smallest:
        smallest = int(digit)

print("Smallest digit:", smallest)