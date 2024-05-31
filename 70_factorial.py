def fact(x): # Функция вычисления факториала числа через рекурсию
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
# print('Введите число: ')
num = int(input('Введите число: '))
print(f"Факториал числа {num} равен {fact(num)}")

