# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

user_number = int(input('Введите количество элементов начального списка: '))

first_list = [randint(1, 100) for i in range(user_number)]
print(first_list)

second_list = [first_list[i + 1] for i in range(len(first_list) - 1) if first_list[i] < first_list[i + 1]]
print(second_list)