# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
a = int(input('Введите количество чисел в списке '))

def numbers(a):
    summ = 0
    for i in range(a):
        n = int(input(f'Введи число {i + 1} '))
        n = (1+1/n)**n
        summ = n + summ
        i += 1
    return summ

print('Сумма чисел равна',round((numbers(a)), 2))