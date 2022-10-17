# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля 
# random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

list = [0, 1, 2 ,3 , 4, 5, 6, 7, 8, 9]
print(list)
for i in range(10):
    variety = list[i]
    j = random.randint(0,9)
    list[i] = list[j]
    list[j] = variety
print(list)