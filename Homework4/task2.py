# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

user_number = int(input('Введите натуральное число:  '))

def find_numbers(user_number):
    i = 2
    result = []
    while i**2 <= user_number:
        while user_number % i == 0:
            result.append(i)
            user_number = user_number / i
        i += 1
    if user_number > 1:
        result.append(int(user_number))
    return result

print('Список простых множителей числа ', user_number, ' равен ', find_numbers(user_number))