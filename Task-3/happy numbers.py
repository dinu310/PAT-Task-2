def find_happy_numbers(n):
    visited = set()
    happy_numbers = []
    
    def helper(num):
        if num == 1:
            return True
        if num in visited:
            return False
        
        visited.add(num)
        return helper(sum(int(digit) for digit in str(num)))
    
    for num in n:
        if helper(num):
            happy_numbers.append(num)
    
    return happy_numbers

input_list = [10,501,22,37,100,999,87,351]
happy_numbers = find_happy_numbers(input_list)
print(len(happy_numbers))
print(happy_numbers,"are happy numbers")

