num = input("Enter number: ")

count = 0
for digit in num:
    if digit == "5":
        count += 1

print("5 occurs:", count, "times")