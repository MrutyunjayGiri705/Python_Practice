n=58329
temp=n
count=0
while n>0:
    count=count+1
    n=n//10

print(count)
n1=str(temp)
print(temp)
print(type(temp))
print(f"First number is {n1[0]}")
print(f"Last number is {n1[count-1]}")
