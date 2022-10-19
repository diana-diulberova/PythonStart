# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

number_of_elements = int(input('Введите количество элементов в списке: '))

def get_list(number_of_elements):
    my_list = sample(range(1, 10), number_of_elements)
    return my_list

def product_of_elements(my_list):
    result = []
    if len(my_list) % 2 == 0:
        length = len(my_list)//2
    else:
        length = len(my_list)//2 + 1
    for i in range(0, length):
        if i != len(my_list) - i - 1:
            product = my_list[i] * my_list[len(my_list) - i - 1]
        else:
            product = my_list[i]
        result.append(product)
    return result

new_list = get_list(number_of_elements)
print(new_list)
print(product_of_elements(new_list))