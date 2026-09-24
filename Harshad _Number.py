num = int(input("Enter number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

if original % total == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")