
vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")
combined = vowels.intersection(set(word))
print(combined)


