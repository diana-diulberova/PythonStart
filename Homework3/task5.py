# 5. ** Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов. 

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

user_number = int(input('Введите число: '))

def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n -2)

def negative_fibonacci(new_list):
    my_list = []
    for i in range(len(new_list)):
        if (len(new_list) - i - 1) % 2 != 0:
            my_list.append(-new_list[-i-1])
        else:
            my_list.append(new_list[-i-1])
    my_list.append(0)
    for i in range(len(new_list)):
        my_list.append(new_list[i])
    return my_list

fibonacci_list = []
for e in range(1, user_number +  1):
    fibonacci_list.append(fibonacci(e))
print(negative_fibonacci(fibonacci_list))