# 4.* Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform

number_of_elements = int(input('Введите количество элементов в списке: '))

def get_my_list(number_of_elements):
    my_list = []
    for i in range(number_of_elements):
        my_list.append(round(uniform(0, 20), 2))
    return my_list

def take_fraction(my_list):
    for i in range(0, len(my_list)):
        my_list[i] = round(my_list[i] - int(my_list[i]), 2)
    return my_list

def find_maximum_and_minimum(my_list):
    maximum = 0
    if my_list[1] > my_list[0]:
        maximum = 1
        minimum = 0
    else:
        minimum = 1
    if len(my_list) > 2:
        for i in range (2, len(my_list)):
            if my_list[i] > my_list[maximum]:
                maximum = i
            elif my_list[i] < my_list[minimum]:
                minimum = i
    result = [maximum, minimum]
    return result

new_list = get_my_list(number_of_elements)
print(new_list)
my_array = take_fraction(new_list)
print(new_list)
min_max = find_maximum_and_minimum(new_list)
print('Разность между максимальным и минимальным значением дробной части элементов равна: ', 
round(new_list[min_max[0]] - new_list[min_max[1]], 2))