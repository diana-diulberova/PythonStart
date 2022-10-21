# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

def test_float (value):
    result_out = True
    try:
        f = float(value)    
    except Exception as e:
        print(e)
        result_out = False
    return result_out

def test_format_float (value):
    result_out = False
    if test_float(value):
       if float(value) == 1/10**(len(value)-2) or float(value) == 0:
            result_out = True
    return result_out


user_number = input('Введите число: ')
while not test_float(user_number):
    user_number = input('Введите число: ')


user_accuracy = input('Введите требуемую точность округления в формате "0.001": ')
while not test_format_float(user_accuracy) :
    print('Ошибка!')
    user_accuracy = input('Введите требуемую точность округления в формате "0.001": ')


if not float(user_accuracy):
    position_accuracy = 0
else:
    position_accuracy = len(user_accuracy)-2

print(f'result -> {float(user_number):.{position_accuracy}f}')