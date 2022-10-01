# Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем как в предыдущем задании). Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def mult_list(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_list = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_list)
from random import randint
a = int(input("Введите количество элементов"))
numbers = [randint(-10, 10) for i in range(1, a+1)]
print(numbers)
mult_list(numbers)