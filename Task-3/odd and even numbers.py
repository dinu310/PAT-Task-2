original_list = [10,501,22,37,100,999,87,351]
even_list = []
odd_list = []
# using For loop to seperate odd list and even list
for i in original_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even number list are :",even_list)
print("odd number list are :",odd_list)
