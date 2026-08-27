n = int(input("Enter n: "))

sum = 0

for i in range(2, n + 1, 2):
    print(f"The even number is {i}")
    sum += i

print("Sum:", sum)