name=input("Enter a name:")
resut=""
count=0
for ch in name:
    if ch!=" ":
        resut=resut+ch
else:
    count+=1

print(resut)
print(count)
