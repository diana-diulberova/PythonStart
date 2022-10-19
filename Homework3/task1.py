# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import sample, randint

number_of_elements = int(input('Введите количество элементов в списке: '))

def get_my_list(number_of_elements):
    my_list = []
    for i in range(number_of_elements):
        my_list.append(randint(0, 9))
    return my_list

def sum_of_elements(my_list):
    sum = 0
    for i in range(0, len(my_list), 2):
        sum = sum + my_list[i]
    return sum

new_list = get_my_list(number_of_elements)
print(new_list)
print(sum_of_elements(new_list))