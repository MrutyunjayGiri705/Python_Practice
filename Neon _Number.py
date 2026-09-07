num=int(input("Enter a number:"))
square=num*num
total=0
while square>0:
    digit=square%10
    total+=digit
    square//=10

if num==total:
    print("The number is Neon number")

else:
    print("The number is not neon number")


