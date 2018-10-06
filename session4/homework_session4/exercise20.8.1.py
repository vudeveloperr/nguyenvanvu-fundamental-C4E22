
letter_counts = { 

}
letter = str(input("enter a string : "))
for letter in letter:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)    