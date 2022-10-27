# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

user_number = int(input('Сколько слов хотите проверить? '))

def new_list(user_number):
    symbols = 'абв'
    result = []
    for i in range(user_number):
        temp = random.sample(symbols, k = 3)
        result.append(''.join(temp))
    my_list = ' '.join(result)
    return my_list

def clean_list(array):
    symbols = 'абв'
    array = array.split(' ')
    for i in array:
        if symbols in array:
            array.remove(symbols)
    my_list = ' '.join(array)
    return my_list

my_list = new_list(user_number)
print(my_list)
print(clean_list(my_list))