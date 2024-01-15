String = input("enter the word :")

# Initialize vowel
vowels = ['A', 'E', 'I', 'O', 'U']

# Convert the text to uppercase to ensure accurate counting
String = String.upper()

print("input string with vowels :",String)

# identify vowels and remove it
for character in String:
    if character in vowels:
        String = String.replace(character,"")
#print the except vowels
print("output string without vowels are :",String)
