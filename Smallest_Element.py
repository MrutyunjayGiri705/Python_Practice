number=[]
size=int(input("Enter the size of the list:"))
for i in range(size):
    number.append(int(input("Enter the element:"))) 
smallest=number[0]
for num in number:
    if num<smallest:
        smallest=num
print("The smallest element is",smallest)   
