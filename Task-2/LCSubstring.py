
def longest_common_substring(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    longest = ""
    #to find the longest common substring 
    for i in range(len(s1)):
        for j in range(i + len(longest), len(s1) + 1):
            substring = s1[i:j]
            if substring in s2:
                longest = substring
            else:
                break

    return longest
print(longest_common_substring(input("enter a string 1 :"),input("enter a string 2 :")))
'''if we enter string 1 and string 2 respectively we will get result.'''