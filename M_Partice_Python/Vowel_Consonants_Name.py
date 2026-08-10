name=input("Enter your name: ")
vowel=0
consonant=0
for i in name:
    if i in "aeiouAEIOU":
        vowel+=1
        print(i,"is a vowel")
    else:
        consonant+=1
        print(i,"is a consonant")
print("Number of vowels: ",vowel)
print("Number of consonants: ",consonant)