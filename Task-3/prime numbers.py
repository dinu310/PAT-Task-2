def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

input_list = [10,501,22,37,100,999,87,351]
prime_numbers = [num for num in input_list if is_prime(num)]
print(prime_numbers)
