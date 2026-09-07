num = int(input("Enter number: "))

total = 0
product = 1

while num > 0:
    digit = num % 10

    total += digit
    product *= digit

    num = num // 10

if total == product:
    print("Spy Number")
else:
    print("Not a Spy Number")