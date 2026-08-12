num=int(input("Enter a Armstrong Number:"))
temp=num
temp1=num
sum=0
count=0
while num>0:
    count+=1
    digit=num%10

    num=num//10

while temp1>0:
    digit=temp1%10
    sum+=digit**count
    temp1=temp1//10

if temp==sum:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")