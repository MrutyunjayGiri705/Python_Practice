number=[]
size=int(input("Enter the size of the list:"))
for i in range(size):
    number.append(int(input("Enter the element:"))) 
largest=number[0]
for num in number:
    if num>largest:
        largest=num
print("The largest element is",largest)   
