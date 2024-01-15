string = input("enter the string :")
#convert the string to set to remove duplicates
unique_chars = set(string)

#count the unique characters
count = len(unique_chars)

#print the unique characters and its count 
print("unique characters in the string :",unique_chars)
print("number of unique characters :",count)
