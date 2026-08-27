number=[]
size=int(input("Enter the size of the list:"))
for i in range(size):
    number.append(int(input("Enter the element:"))) 
even=0
odd=0
for num in number:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:",even)
print("Odd numbers:",odd)