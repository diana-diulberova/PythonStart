# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

# user_number = int(input('Введите число для преобразования: '))
# new_number = ''
# while user_number > 0:
#     new_number = str(user_number % 2) + new_number
#    user_number = user_number // 2
# print(f'Преобразованное двоичное число: {new_number}')

user_number = int(input('Введите число для преобразования: '))

def conversion(number):
    result = []
    while number > 0:
        remains = number % 2
        number = number // 2
        result.append(remains)
    result.reverse()
    return result

new_number = conversion(user_number)
for i in range(len(new_number)):
    print(new_number[i], end = '')