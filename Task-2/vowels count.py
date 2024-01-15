String = input("enter the word :")

# Initialize vowel counts
vowels = ['A', 'E', 'I', 'O', 'U']
vowel_counts = {vowel: 0 for vowel in vowels}
total_vowels = 0

# Convert the text to uppercase to ensure accurate counting
String = String.upper()

# Count the vowels
for character in String:
    if character in vowels:
        vowel_counts[character] += 1
        total_vowels += 1
#print the total number of vowels
print("total vowels are :",total_vowels)
#print the each vowel count respectively
print("count of each vowel",vowel_counts)
