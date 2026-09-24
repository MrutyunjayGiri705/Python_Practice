name=input("Enter a name:")
uppercase=0
lowercase=0
for ch in name:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1

print(uppercase)
print(lowercase)



