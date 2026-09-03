words = ["cat", "elephant", "dog", "tiger"]

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)