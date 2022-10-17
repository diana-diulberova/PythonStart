# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и 
# выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

str = input('Введите натуральное число n: ')


n = int(str)
list = []

for i in range(1,n+1,1):
    list.append(round((1+1/i)**i))

sum = 0    
for i in list:
    sum += i

print(f'{list} -> {sum}')