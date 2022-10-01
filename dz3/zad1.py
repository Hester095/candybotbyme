# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
a = int(input("Введите количество элементов"))
numbers = [randint(-10, 10) for i in range(1, a+1)]
print(numbers)
summ = 0
for i in range(1, len(numbers)):
    if i % 2 == 1:
        summ += numbers[i]
print(summ)