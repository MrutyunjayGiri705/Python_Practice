# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)  
# numbers = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# print(numbers) 
# pairs = [(x, y) for x in range(2) for y in range(3)]
# print(pairs) 
# words = ["hello", "world", "python"]
# upper_words = [word.upper() for word in words]
# print(upper_words)  
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened) 
unique_numbers = {x for x in [1, 2, 2, 3, 4, 4]}
print(unique_numbers)
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict) 