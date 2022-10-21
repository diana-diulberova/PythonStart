# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import randrange


def list_numbers(count: int):
    if count < 0: 
        print("Ошибка! Количество чисел не может быть отрицательным.")
        return []

    list_numbers = []
    for i in range(count):
        list_numbers.append(randrange(count))

    return list_numbers


def uniq_element(list_numbers: list):
    result = []
    my_array = {}.fromkeys(list_numbers, 0)

    for i in list_numbers:
        my_array[i] += 1

    for k in my_array:
        if my_array[k] == 1:
            result.append(k)

    return result


new_list = list_numbers(int(input("Введите количество элементов списка: ")))
print(new_list)
print(uniq_element(new_list))