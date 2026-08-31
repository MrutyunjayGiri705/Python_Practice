num = int(input("Enter number: "))

root = int(num ** 0.5)

if root * root == num:
    print("Perfect Square")
else:
    print("Not Perfect Square")