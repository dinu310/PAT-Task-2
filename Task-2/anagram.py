''''validate the strings are anagram or not
*strings should be equal character length and it can same or different order

'''
str1 = input("enter string1 :")
str2 = input("enter string2 :")

#to check the strings are anagram or not
if len(str1)!= len(str2):
    print("the strings are not anagram")
else:
    if sorted(str1) == sorted(str2):
        print("the strings are anagrams")
    else:
        print("strings are not anagram")
