char = input("input string")
frequency = {}
for char in char:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
max_freq_char = max(frequency, key=frequency.get)
print("most frequent character is :",max_freq_char)
